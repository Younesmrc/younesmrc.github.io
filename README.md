# Younes Arjdal — Portfolio V1

Portfolio personnel statique (HTML / CSS / JavaScript léger), conçu pour être publié gratuitement avec GitHub Pages.

## Structure

```text
younesmrc.github.io/
├── index.html
├── style.css
├── script.js
├── .nojekyll
├── README.md
└── assets/
    ├── favicon.svg
    └── Younes-Arjdal-CV.pdf
```

## Lancer le site localement

Le site ne nécessite aucune installation ni aucun framework.

Option la plus simple : ouvrir `index.html` dans un navigateur.

Pour un petit serveur local (optionnel) :

```bash
python -m http.server 8000
```

Puis ouvrir `http://localhost:8000`.

## Publication sur GitHub Pages

Le compte GitHub cible est `younesmrc`. Pour obtenir exactement l'URL :

```text
https://younesmrc.github.io
```

le repository doit s'appeler :

```text
younesmrc.github.io
```

C'est le nom réservé par GitHub Pages pour le **site utilisateur** du compte `younesmrc`. Un repository portant un autre nom créerait plutôt un site de projet avec une URL du type `https://younesmrc.github.io/nom-du-repository/`.

### 1. Créer le repository

1. Connecte-toi à GitHub avec le compte `younesmrc`.
2. Clique sur **New repository**.
3. Dans **Repository name**, saisis exactement `younesmrc.github.io`.
4. Choisis **Public** (solution gratuite avec GitHub Pages sur GitHub Free).
5. Crée le repository sans ajouter de fichier initial : le premier upload créera la branche `main`.

### 2. Ajouter les fichiers

Upload à la racine du repository le contenu de ce dossier :

- `index.html`
- `style.css`
- `script.js`
- `.nojekyll`
- `README.md`
- le dossier `assets/`

Important : `index.html` doit être à la racine du repository, et non dans un sous-dossier supplémentaire.

### 3. Activer GitHub Pages

1. Ouvre le repository `younesmrc.github.io`.
2. Va dans **Settings**.
3. Dans le menu de gauche, ouvre **Pages**.
4. Dans **Build and deployment**, choisis **Deploy from a branch**.
5. Dans **Branch**, sélectionne `main`.
6. Dans le sélecteur de dossier, sélectionne `/(root)`.
7. Clique sur **Save**.

### 4. Vérifier le déploiement

Après le déploiement, GitHub affiche dans **Settings → Pages** l'adresse du site.

URL finale :

```text
https://younesmrc.github.io
```

Le premier déploiement GitHub Pages peut prendre quelques minutes. Son état est visible dans l'onglet **Actions** et dans **Settings → Pages**.

## Où modifier le contenu

### Présentation / titre / stage recherché

Dans `index.html`, section :

```html
<section id="home" ...>
```

### Projets

Dans `index.html`, section :

```html
<section id="projects" ...>
```

Chaque projet est un bloc :

```html
<article class="project-card">
```

Tu peux dupliquer ou supprimer ces blocs.

### Compétences

Dans `index.html`, section `#skills`.

### Formation

Dans `index.html`, section `#education`.

### Liens GitHub / LinkedIn / email

Cherche simplement :

- `https://github.com/younesmrc`
- `https://linkedin.com/in/younes-arjdal-1906b8231`
- `mailto:younesarjdal@yahoo.com`

### CV

Le bouton CV pointe vers :

```text
assets/Younes-Arjdal-CV.pdf
```

Pour remplacer le CV, remplace ce fichier en conservant le même nom. Sinon, modifie le lien dans `index.html`.

### Couleurs

Dans `style.css`, tout en haut, les variables CSS sont regroupées dans `:root` :

```css
:root {
  --navy-950: ...;
  --navy-900: ...;
  --blue-700: ...;
  ...
}
```

Modifier ces valeurs suffit pour changer la palette générale.

### Images

La V1 n'utilise volontairement aucune photo ou illustration. Pour en ajouter plus tard :

1. place les fichiers dans `assets/` ;
2. ajoute une balise `<img>` dans `index.html` ;
3. ajoute le style correspondant dans `style.css`.

## Mise à jour du site

Chaque modification poussée sur la branche `main` est redéployée automatiquement par GitHub Pages.
