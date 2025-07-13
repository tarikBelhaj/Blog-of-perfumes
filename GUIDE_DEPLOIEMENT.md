# 🚀 Guide de Déploiement - Parfums de Dubaï

Ce guide vous explique comment déployer votre site e-commerce de parfums de Dubaï sur GitHub Pages.

## 📋 Pré-requis

- Compte GitHub
- Git installé sur votre ordinateur
- Éditeur de code (VS Code recommandé)

## 🗂️ Structure du Projet

```
parfums-dubai/
├── _config.yml              # Configuration Jekyll
├── _posts/                  # Articles de blog
│   └── 2025-01-13-mon-experience-lattafa-pepites-2025.md
├── _products/               # Pages produits
│   ├── lattafa-khamrah.md
│   └── lattafa-asad.md
├── categories/              # Pages catégories
│   └── parfums-oud.md
├── assets/                  # Images et ressources
│   └── images/
│       ├── products/
│       ├── blog/
│       ├── categories/
│       └── about/
├── index.md                 # Page d'accueil
├── about.md                 # À propos
├── contact.md               # Contact
├── Gemfile                  # Dépendances Jekyll
├── README.md                # Documentation
└── GUIDE_DEPLOIEMENT.md     # Ce guide
```

## 🚀 Étapes de Déploiement

### 1. Créer le Repository GitHub

```bash
# Créer un nouveau repository sur GitHub
# Nom suggéré: parfums-dubai-site
```

### 2. Cloner et Pousser le Projet

```bash
# Cloner le repository vide
git clone https://github.com/VOTRE-USERNAME/parfums-dubai-site.git
cd parfums-dubai-site

# Copier tous les fichiers du projet dans ce dossier
# Puis ajouter tous les fichiers
git add .
git commit -m "🎉 Initial commit - Site parfums de Dubaï"
git push origin main
```

### 3. Activer GitHub Pages

1. Aller dans les **Settings** du repository
2. Scroller jusqu'à **Pages**
3. Dans **Source**, sélectionner **Deploy from a branch**
4. Choisir **main** comme branche
5. Sélectionner **/ (root)** comme dossier
6. Cliquer sur **Save**

### 4. Configuration Personnalisée

Éditez `_config.yml` pour personnaliser :

```yaml
title: "Votre Nom de Boutique"
description: "Votre description personnalisée"
url: "https://votre-username.github.io"
baseurl: "/parfums-dubai-site"
```

### 5. Personnaliser les Informations

#### Contact
Modifiez `contact.md` avec vos vraies informations :
- Numéro de téléphone
- Email
- Adresse si applicable

#### À Propos
Personnalisez `about.md` avec :
- Votre histoire personnelle
- Vos motivations
- Votre expertise

#### Réseaux Sociaux
Mettez à jour les liens dans `_config.yml`

## 🖼️ Gestion des Images

### Structure recommandée :
```
assets/images/
├── products/                # Images produits
│   ├── lattafa-khamrah.jpg
│   └── lattafa-asad.jpg
├── blog/                    # Images articles
│   └── lattafa-pepites-2025.jpg
├── categories/              # Images catégories
│   └── parfums-oud-banner.jpg
└── about/                   # Images pages statiques
    └── about-banner.jpg
```

### Optimisation :
- Format : JPG pour les photos, PNG pour les logos
- Taille : 1200x800px pour les images principales
- Compression : Optimisées pour le web (< 200KB)

## 🎨 Personnalisation du Design

### Thème par défaut
Le site utilise le thème **Minima** de Jekyll, mais vous pouvez :

1. **Customiser les couleurs** : Créer `assets/css/style.scss`
2. **Modifier les layouts** : Créer `_layouts/` avec vos templates
3. **Ajouter des composants** : Créer `_includes/` pour les éléments réutilisables

### Exemple de personnalisation CSS :

```css
/* assets/css/style.scss */
---
---

@import "minima";

:root {
  --primary-color: #d4af37;
  --secondary-color: #8b4513;
  --text-color: #333;
}

.site-header {
  background-color: var(--primary-color);
}
```

## 📈 Optimisation SEO

### Vérifications importantes :
- [ ] Tous les Front Matter sont complets
- [ ] Descriptions uniques pour chaque page
- [ ] Images avec alt text
- [ ] URL propres et descriptives
- [ ] Sitemap généré automatiquement

### Plugins activés :
- `jekyll-seo-tag` : Méta-données automatiques
- `jekyll-sitemap` : Plan du site
- `jekyll-feed` : Flux RSS

## 🔧 Dépannage

### Erreurs communes :

1. **Site ne se charge pas** : Vérifiez l'URL et le baseurl dans `_config.yml`
2. **Images manquantes** : Vérifiez les chemins relatifs
3. **Erreur de build** : Consultez l'onglet **Actions** sur GitHub

### Logs de build :
- GitHub Actions > Pages build and deployment
- Consultez les erreurs Jekyll

## 📱 Test Local

Pour tester localement avant de pousser :

```bash
# Installer les dépendances
bundle install

# Lancer le serveur de développement
bundle exec jekyll serve

# Ouvrir http://localhost:4000
```

## 🌐 Domaine Personnalisé (Optionnel)

1. Acheter un domaine (ex: parfums-dubai.fr)
2. Configurer les DNS vers GitHub Pages
3. Ajouter un fichier `CNAME` avec votre domaine
4. Activer HTTPS dans les settings

## 📊 Analytics et Suivi

### Google Analytics :
1. Créer un compte GA4
2. Ajouter le tracking ID dans `_config.yml`
3. Inclure le code dans `_includes/head.html`

### Google Search Console :
1. Ajouter et vérifier votre site
2. Soumettre le sitemap
3. Surveiller les performances

## 🚀 Commandes Git Utiles

```bash
# Vérifier le statut
git status

# Ajouter des modifications
git add .
git commit -m "📝 Mise à jour contenu"
git push origin main

# Créer une nouvelle branche
git checkout -b nouvelle-fonctionnalite

# Fusionner une branche
git checkout main
git merge nouvelle-fonctionnalite
```

## 📝 Maintenance Régulière

### Choses à faire régulièrement :
- [ ] Mettre à jour les produits
- [ ] Publier de nouveaux articles
- [ ] Vérifier les liens cassés
- [ ] Optimiser les images
- [ ] Surveiller les performances

### Sauvegarde :
- Le code est sur GitHub (sauvegardé automatiquement)
- Exportez régulièrement votre contenu
- Gardez une copie locale

## 🎯 Prochaines Étapes

1. **Contenu** : Ajouter plus de produits et articles
2. **Design** : Personnaliser l'apparence
3. **Fonctionnalités** : Ajouter un système de commande
4. **Marketing** : Optimiser pour le référencement

---

**Félicitations ! Votre site est maintenant prêt à être déployé. Suivez ce guide étape par étape pour mettre en ligne votre boutique de parfums de Dubaï.**

**URL de votre site :** `https://votre-username.github.io/parfums-dubai-site`

---

*Pour toute question, consultez la documentation Jekyll ou créez une issue sur GitHub.*