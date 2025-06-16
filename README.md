# 🏠 Orange County Lettings

Site web de location immobilière pour Orange County, développé en Django.

## 📚 Documentation Complète

Pour une documentation détaillée incluant l’architecture, le guide d’installation, les technologies utilisées, et bien plus :

👉 [Consultez la documentation sur Read the Docs](https://oclettings.readthedocs.io/) *(Remplacez par le lien exact si nécessaire)*

---

## 🚀 Aperçu

Orange County Lettings permet :
- La consultation de locations (`lettings`)
- La gestion de profils utilisateurs (`profiles`)

Le projet utilise :
- **Django** comme framework web
- **SQLite** comme base de données en développement
- **Docker** pour le déploiement via Render.com

---

## 💻 Développement Local

### 🔧 Prérequis

- Git CLI
- Python 3.9 ou supérieur *(vérifiez `runtime.txt` pour la version exacte)*
- SQLite3 CLI *(optionnel)*

### 🛠 Installation

Clonez le dépôt :

```bash
git clone https://github.com/siwax74/P14_DJANGO_PIPELINE_CI_CD.git
cd P14_DJANGO_PIPELINE_CI_CD
```

Créez et activez un environnement virtuel :

**macOS / Linux :**
```bash
python3 -m venv env
source venv/bin/activate
```

**Windows (PowerShell) :**
```powershell
python -m venv env
.env\Scripts\Activate.ps1
```

Installez les dépendances :

```bash
pip install -r requirements.txt
```

Appliquez les migrations :

```bash
python manage.py migrate
```

Lancez le serveur :

```bash
python manage.py runserver
```

Accédez au site : [http://localhost:8000](http://localhost:8000)

---

## 🧪 Outils de Qualité

### 🔍 Linting (Flake8)

```bash
flake8 .
```

### ✅ Tests Unitaires (Pytest)

```bash
pytest
```

### 📊 Couverture de Code

```bash
pytest --cov=.
```

---

## 🗃 Base de Données

- Fichier SQLite local : `oc-lettings-site.sqlite3`
- Inspection possible avec :
  - `sqlite3` (CLI)
  - [DB Browser for SQLite](https://sqlitebrowser.org/)

---

## 🔐 Panel d’Administration Django

Accessible via : [http://localhost:8000/admin/](http://localhost:8000/admin/)

Créez un superutilisateur si nécessaire :

```bash
python manage.py createsuperuser
```

---

## 🚢 Déploiement CI/CD

Le projet utilise **GitHub Actions** pour :

- Construire une image Docker
- Déployer automatiquement sur **Render.com**

### ⚙️ Secrets GitHub à Configurer

Dans `Settings > Secrets and variables > Actions` du dépôt :

| Nom               | Description |
|------------------|-------------|
| `SECRET_KEY`      | Clé secrète Django (générable avec `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`) |
| `SENTRY_DSN`      | *(Optionnel)* DSN pour le suivi des erreurs avec Sentry |
| `DOCKERHUB_USERNAME` | Nom d'utilisateur Docker Hub |
| `DOCKERHUB_TOKEN` | Token d’accès Docker Hub |
| `RENDER_WEBHOOK`  | URL du "Deploy Hook" de Render |

Voir le fichier [`ci_cd.yml`](.github/workflows/ci_cd.yml) pour plus de détails.

---

## 🧾 Licence

Projet sous licence MIT – voir le fichier [LICENSE](LICENSE) pour plus d’informations.

---

## 🙌 Remerciements

Projet développé dans le cadre du parcours développeur Python chez OpenClassrooms.