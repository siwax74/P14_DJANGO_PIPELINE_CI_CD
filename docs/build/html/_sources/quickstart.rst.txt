Guide de démarrage rapide
==========================

Ce guide vous permet de faire fonctionner rapidement l'application localement pour développement ou test.

Option 1 : Démarrage local (avec Python)
----------------------------------------

1. **Cloner le projet**

.. code-block:: bash

   git clone https://github.com/votre-utilisateur/oc-lettings.git
   cd oc-lettings

2. **Créer et activer un environnement virtuel**

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows

3. **Installer les dépendances**

.. code-block:: bash

   pip install -r requirements.txt

4. **Exécuter les migrations**

.. code-block:: bash

   python manage.py migrate

5. **Lancer le serveur de développement**

.. code-block:: bash

   python manage.py runserver

6. **Accéder au site**

- Front-end : http://127.0.0.1:8000  
- Interface admin : http://127.0.0.1:8000/admin

Option 2 : Démarrage rapide avec Docker
----------------------------------------

1. **Construire l’image Docker**

.. code-block:: bash

   docker build -t oc-lettings:latest .

2. **Lancer le conteneur**

.. code-block:: bash

   docker run -d -p 8000:8000 \
     -e DEBUG=0 \
     -e SECRET_KEY='votre_clé' \
     -e ALLOWED_HOSTS='*' \
     oc-lettings:latest

3. **Accéder à l'application**

- Accès : http://localhost:8000

Créer un superutilisateur (si nécessaire) via :

.. code-block:: bash

   docker exec -it <container_id> python manage.py createsuperuser

Vérification rapide
-------------------

✅ Lancement du site sans erreur  
✅ Accès aux modules "lettings" et "profiles"  
✅ Interface admin fonctionnelle  
✅ Pages d’erreur 404/500 personnalisées (testables manuellement)

