# Portfolio Christ Strauss Kimbata — Version 2

Design responsive bleu nuit / vert émeraude, Django 5.2, CSS local sans dépendance CDN, illustrations techniques SVG.

## Démarrer (Windows PowerShell)

Ouvrir le dossier contenant `manage.py` :

```powershell
py -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py makemigrations portfolio
python manage.py migrate
python manage.py seed_projects
python manage.py runserver
```

Visiter http://127.0.0.1:8000/

## Mettre à jour depuis la V1 sans perdre les données

1. Arrêter le serveur (`Ctrl+C`).
2. **Sauvegarder** `db.sqlite3` et toutes les modifications personnelles de la V1.
3. Copier les dossiers `templates/` et `static/` de la V2 vers votre dossier `portfolio_kimbata` de la V1, en remplaçant les anciens fichiers. Les modèles Python et la base ne changent pas.
4. Relancer `python manage.py runserver`. Aucun besoin de recréer la base.

## Votre portrait

Mettre votre photo dans `static/images/portrait.jpg`, puis dans `templates/portfolio/home.html`, remplacer `images/portrait.svg` par `images/portrait.jpg`. Choisir une photo verticale et autorisée à être publiée.

## Images et configurations des projets

Les images SVG sous `static/images/projects/` sont des **schémas pédagogiques**, pas des captures d'infrastructures réelles. Remplacez-les par vos schémas ou captures de lab anonymisées (sans IP publiques, secrets, noms de clients, accès internes). Pour garder les chemins actuels, conservez les noms de fichiers SVG ou adaptez les balises `img` dans les templates.

## Personnalisation

- Textes de la page d'accueil : `templates/portfolio/home.html`
- Couleurs / styles : `static/css/style.css`
- Projets : admin Django (`python manage.py createsuperuser`, puis `/admin/`) ou `portfolio/management/commands/seed_projects.py`
- Attention : la commande `seed_projects` met à jour les six projets par défaut, ne pas la relancer après modifications manuelles sans en vérifier les effets.
- La section Articles présente des idées **à publier**, elle ne prétend pas qu'elles sont déjà en ligne.

## Déploiement

Configuration locale de développement uniquement. Avant publication : clé secrète par variable d'environnement, `DEBUG=0`, hôtes autorisés, HTTPS, gestion de fichiers statiques et revue de sécurité.
