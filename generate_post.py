import openai
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
import schedule
import time
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration de l'API OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_blog_post(topic):
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=f"Écris un article de blog détaillé sur {topic}.",
        max_tokens=1000
    )
    return response.choices[0].text.strip()

# Configuration de la connexion WordPress
wp = Client(os.getenv('WORDPRESS_URL'), os.getenv('WORDPRESS_USERNAME'), os.getenv('WORDPRESS_PASSWORD'))

def post_to_wordpress(title, content):
    post = WordPressPost()
    post.title = title
    post.content = content
    post.post_status = 'publish'
    wp.call(NewPost(post))

def job():
    topic = "bienfaits du yoga pour la santé"
    content = generate_blog_post(topic)
    post_to_wordpress(topic, content)

# Planifier la publication automatique
schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


