Déploiement
===========

Vue d’ensemble
--------------

Le déploiement de ce projet repose sur un pipeline CI/CD automatisé qui garantit la qualité du code, la création d’une image Docker, puis son déploiement sur un environnement de production.

Seules les modifications apportées à la branche ``master`` déclenchent automatiquement la conteneurisation et le déploiement du site.

Configuration requise
----------------------

Pour que le déploiement fonctionne correctement, les éléments suivants doivent être configurés :

- **Docker** installé localement ou sur l’environnement distant.
- **Compte Docker Hub** valide pour publier les images Docker.
- **Hébergeur** compatible Docker (ex : Render, AWS Elastic Beanstalk, Azure Web App).
- **Outil CI/CD** (GitHub Actions, GitLab CI, etc.) configuré avec :
  
  - Secrets : ``DOCKER_USERNAME``, ``DOCKER_PASSWORD``, ``SENTRY_DSN``, etc.
  - Accès au registre Docker Hub.

- **Variables d’environnement** dans l’hébergeur (à ne pas inclure dans le code) :

  - ``SECRET_KEY``
  - ``SENTRY_DSN``
  - ``DEBUG``
  - ``ALLOWED_HOSTS``
  - ``DATABASE_URL`` (si base distante)

Étapes du pipeline CI/CD
-------------------------

1. **Compilation et tests** *(déclenché sur toutes les branches)*

   - Exécution de ``flake8`` pour le linting.
   - Exécution des tests via ``pytest``.
   - Vérification que la couverture est ≥ 80 %.

2. **Conteneurisation** *(uniquement sur ``main``)*

   - Construction d’une image Docker.
   - Push de l’image sur Docker Hub (tag : ``<commit-hash>``).

3. **Déploiement** *(si la conteneurisation réussit)*

   - Récupération de l’image Docker.
   - Lancement du site sur l’hébergeur choisi.
   - Chargement vérifié des fichiers statiques.
   - Configuration sécurisée via variables d’environnement.

Déploiement manuel (local)
---------------------------

Pour effectuer un déploiement manuel local avec Docker :

.. code-block:: bash

   # Cloner le projet
   git clone https://github.com/siwax74/oc-lettings.git
   cd oc-lettings

   # Construire l’image Docker
   docker build -t oc-lettings:latest .

   # Lancer le conteneur
   docker run -d -p 8000:8000 \
     -e DEBUG=0 \
     -e SECRET_KEY='votre_clé' \
     -e SENTRY_DSN='https://...' \
     -e ALLOWED_HOSTS='*' \
     oc-lettings:latest

Accès au site après déploiement
--------------------------------

- Interface admin : ``https://votresite.onrender.com``
- Vérification : chargement des fichiers CSS/JS/images
- Monitoring : les erreurs doivent apparaître dans Sentry

Points de contrôle post-déploiement
------------------------------------

- ✔ Apparence identique à l’environnement local
- ✔ Accès aux routes ``lettings``, ``profiles``, ``index``
- ✔ Pages d’erreur 404 et 500 personnalisées
- ✔ Vérification des logs dans Sentry
