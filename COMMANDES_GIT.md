# 🚀 Comment Pusher Votre Projet sur GitHub

## 📋 Étapes Rapides

### 1. Créer un nouveau repository sur GitHub
1. Aller sur [github.com](https://github.com)
2. Cliquer sur **New repository**
3. Nom suggéré : `parfums-dubai-site`
4. Cocher **Public** 
5. Ne pas cocher "Add a README file"
6. Cliquer **Create repository**

### 2. Initialiser Git dans votre dossier de projet

```bash
# Aller dans le dossier de votre projet
cd /chemin/vers/votre/projet

# Initialiser git
git init

# Ajouter tous les fichiers
git add .

# Premier commit
git commit -m "🎉 Initial commit - Site parfums de Dubaï"

# Ajouter l'origine (remplacez VOTRE-USERNAME par votre nom d'utilisateur GitHub)
git remote add origin https://github.com/VOTRE-USERNAME/parfums-dubai-site.git

# Pousser vers GitHub
git push -u origin main
```

### 3. Activer GitHub Pages

1. Aller dans **Settings** de votre repository
2. Scroller jusqu'à **Pages**
3. Dans **Source** : sélectionner **Deploy from a branch**
4. Branche : **main**
5. Dossier : **/ (root)**
6. Cliquer **Save**

### 4. Votre site sera accessible à :
```
https://VOTRE-USERNAME.github.io/parfums-dubai-site
```

## 🔧 Si vous avez des problèmes

### Erreur : remote origin already exists
```bash
git remote remove origin
git remote add origin https://github.com/VOTRE-USERNAME/parfums-dubai-site.git
```

### Erreur : branch main doesn't exist
```bash
git branch -M main
git push -u origin main
```

### Mettre à jour après modifications
```bash
git add .
git commit -m "📝 Mise à jour du contenu"
git push origin main
```

## 📱 Commandes Git Utiles

```bash
# Vérifier le statut
git status

# Voir l'historique
git log --oneline

# Créer une nouvelle branche
git checkout -b nouvelle-fonctionnalite

# Revenir à main
git checkout main

# Voir les branches
git branch -a
```

---

**🎉 Félicitations ! Votre site est maintenant en ligne sur GitHub Pages !**

**⏰ Temps d'attente :** 5-10 minutes pour que GitHub Pages génère votre site

**🔗 URL finale :** https://VOTRE-USERNAME.github.io/parfums-dubai-site