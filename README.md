# Blog des Parfums 🌸

Un blog automatisé et moderne dédié à l'univers des parfums, construit avec Jekyll et déployé automatiquement sur GitHub Pages.

## 🎯 À Propos

Ce projet vise à automatiser au maximum la génération et la publication d'articles de blog sur les parfums en utilisant l'API OpenAI et GitHub. Le blog propose des critiques, guides d'achat et conseils dans le monde des fragrances.

## ✨ Fonctionnalités

- **Design moderne et responsive** avec animations CSS
- **Structure organisée** avec layouts Jekyll optimisés
- **Navigation intuitive** avec pages dédiées
- **Génération automatisée** de contenu avec l'IA
- **Déploiement automatique** sur GitHub Pages
- **Formulaire de contact** fonctionnel
- **SEO optimisé** avec métadonnées appropriées

## 🚀 Installation et Configuration

### Prérequis

- Ruby (version 2.7+)
- Bundler
- Git

### Installation

1. **Clonez le dépôt :**
   ```bash
   git clone https://github.com/tarikBelhaj/Blog-of-perfumes.git
   cd Blog-of-perfumes
   ```

2. **Installez les dépendances :**
   ```bash
   bundle install
   ```

3. **Lancez le serveur de développement :**
   ```bash
   bundle exec jekyll serve
   ```

4. **Accédez au site :**
   Ouvrez votre navigateur sur `http://localhost:4000`

### Configuration pour la génération automatique

1. **Installez les dépendances Python :**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configurez vos clés API :**
   - Créez un fichier `.env` avec votre clé OpenAI
   - Ajoutez vos secrets GitHub pour le déploiement automatique

## 📁 Structure du Projet

```
Blog-of-perfumes/
├── _layouts/           # Templates Jekyll
│   ├── default.html    # Layout principal
│   └── post.html       # Layout pour les articles
├── _posts/             # Articles du blog
├── assets/
│   └── css/
│       └── style.css   # Styles CSS modernes
├── about.html          # Page À Propos
├── blog.html           # Liste des articles
├── contact.html        # Page de contact
├── index.html          # Page d'accueil
├── _config.yml         # Configuration Jekyll
├── generate_post.py    # Script de génération automatique
└── README.md           # Ce fichier
```

## 🎨 Personnalisation

### Couleurs et Thème

Les couleurs principales sont définies dans `assets/css/style.css` :
- Gradient principal : `#667eea` vers `#764ba2`
- Arrière-plan : Gradient de `#f5f7fa` vers `#c3cfe2`

### Contenu

1. **Articles :** Placez vos fichiers Markdown dans `_posts/`
2. **Configuration :** Modifiez `_config.yml` pour personnaliser le site
3. **Pages :** Éditez les fichiers HTML à la racine pour personnaliser les pages

## 🤖 Génération Automatique

Le script `generate_post.py` permet de générer automatiquement des articles :

```bash
python generate_post.py
```

### Configuration OpenAI

Assurez-vous d'avoir configuré votre clé API OpenAI dans les variables d'environnement.

## 🌐 Déploiement

Le site est automatiquement déployé sur GitHub Pages à chaque push sur la branche `main`.

**URL du site :** [https://tarikBelhaj.github.io/Blog-of-perfumes](https://tarikBelhaj.github.io/Blog-of-perfumes)

## 📱 Responsive Design

Le site est entièrement responsive et optimisé pour :
- 📱 Mobiles (320px+)
- 📟 Tablettes (768px+)
- 💻 Desktop (1200px+)

## 🛠️ Technologies Utilisées

- **Jekyll** - Générateur de site statique
- **CSS3** - Animations et design moderne
- **GitHub Pages** - Hébergement
- **OpenAI API** - Génération de contenu
- **Python** - Scripts d'automatisation

## 📧 Contact

- **Email :** [belhajweb.contact@gmail.com](mailto:belhajweb.contact@gmail.com)
- **GitHub :** [@tarikBelhaj](https://github.com/tarikBelhaj)

## 📄 License

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🎉 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Forker le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

---

*Créé avec ❤️ par [Tarik Belhaj](https://github.com/tarikBelhaj)*
