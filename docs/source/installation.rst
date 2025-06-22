Installation du projet
======================

Prérequis
---------

Avant d’installer le projet, assurez-vous que les éléments suivants sont installés sur votre machine :

- Python >= 3.9
- pip (Python package manager)
- virtualenv (fortement recommandé)
- Git
- Docker (optionnel, pour tests et déploiement conteneurisé)

Étapes d'installation
----------------------

1. **Cloner le dépôt**

.. code-block:: bash

   git clone https://github.com/votre-utilisateur/oc-lettings.git
   cd oc-lettings

2. **Créer et activer un environnement virtuel**

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate  # sous Linux/macOS
   venv\Scripts\activate     # sous Windows

3. **Installer les dépendances**

.. code-block:: bash

   pip install -r requirements.txt

4. **Configurer les variables d’environnement**

Créez un fichier `.env` ou exportez manuellement les variables nécessaires :

- ``SECRET_KEY`` : une clé secrète Django
- ``DEBUG`` : 1 pour le mode développement
- ``SENTRY_DSN`` : (optionnel en local, nécessaire pour Sentry)
- ``ALLOWED_HOSTS`` : par défaut `localhost` ou `127.0.0.1`

5. **Appliquer les migrations**

.. code-block:: bash

   python manage.py migrate

6. **Créer un superutilisateur (accès admin)**

.. code-block:: bash

   python manage.py createsuperuser

7. **Lancer le serveur local**

.. code-block:: bash

   python manage.py runserver

Vous pouvez ensuite accéder à l'application à l'adresse :  
http://127.0.0.1:8000

8. **(Optionnel) Tester le projet localement avec Docker**

.. code-block:: bash

   docker build -t oc-lettings:local .
   docker run -d -p 8000:8000 oc-lettings:local

Structure des fichiers
----------------------

- ``requirements.txt`` : dépendances Python
- ``manage.py`` : interface principale Django
- ``oc_lettings_site/`` : configuration principale du projet
- ``lettings/`` et ``profiles/`` : applications Django modularisées
- ``templates/`` : templates HTML classés par application
- ``static/`` : fichiers statiques (CSS, images, JS)

