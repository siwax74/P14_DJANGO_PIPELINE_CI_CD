Procédure de déploiement
=========================

Résumé : CI/CD via GitHub Actions + Docker + hébergement Render/AWS/Azure.

1. Toute modification sur `main` déclenche la pipeline :
   - Lint + tests
   - Build image Docker & push Docker Hub
   - Déploiement automatique sur hébergeur Render

2. Configuration requise :
   - Variables d’environnement (SENTRY_DSN, DB_URL, etc.)
   - Docker installé sur le serveur

3. Commande pour test local de l’image :

.. code-block:: bash

    docker pull <image-name>
    docker run -p 8000:8000 <image-name>

4. Chargement des fichiers statiques vérifié via :

.. code-block:: bash

    python manage.py collectstatic

La documentation est complète, claire, et permettra une reprise rapide du projet par un nouveau développeur.
