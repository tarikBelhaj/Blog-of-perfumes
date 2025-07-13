import ast
import types
import unittest
from unittest.mock import MagicMock, patch


def load_generate_blog_post(openai_module):
    """Load only the generate_blog_post function without executing the rest."""
    with open('generate_post.py', 'r') as f:
        tree = ast.parse(f.read(), filename='generate_post.py')
    func = next(
        node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'generate_blog_post'
    )
    module = ast.Module(body=[func], type_ignores=[])
    namespace = {'openai': openai_module}
    exec(compile(module, 'generate_post.py', 'exec'), namespace)
    return namespace['generate_blog_post']


class TestGenerateBlogPost(unittest.TestCase):
    def setUp(self):
        completion_class = types.SimpleNamespace(create=lambda *a, **k: None)
        self.openai = types.SimpleNamespace(Completion=completion_class)
        self.generate_blog_post = load_generate_blog_post(self.openai)

    def test_generate_blog_post_returns_response_text(self):
        expected = 'Mocked blog post'
        mock_resp = MagicMock()
        mock_resp.choices = [MagicMock(text=f' {expected} ')]
        with patch.object(self.openai.Completion, 'create', return_value=mock_resp) as mock_create:
            result = self.generate_blog_post('test topic')
        self.assertEqual(result, expected)
        mock_create.assert_called_once_with(
            engine='text-davinci-004',
            prompt='Écris un article de blog détaillé sur test topic.',
            max_tokens=1000,
        )


if __name__ == '__main__':
    unittest.main()
