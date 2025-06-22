Technologies et outils utilisés
===============================

Langages de programmation
--------------------------

- **Python 3.12+** : Langage principal utilisé pour le développement backend avec Django.
- **HTML / CSS** : Utilisés pour les templates et le rendu visuel du site.

Frameworks et bibliothèques
----------------------------

- **Django** : Framework web principal utilisé pour construire l'application (MVC, ORM, admin, etc.).
- **Gunicorn** : Serveur WSGI utilisé pour le déploiement en production.
- **pytest** : Utilisé pour les tests unitaires et d’intégration.
- **flake8** : Outil de linting pour garantir la qualité et la cohérence du code.
- **Sentry SDK** : Intégré pour la remontée des erreurs et la surveillance du comportement en production.
- **python-decouple** : Gestion des variables d’environnement (séparation configuration / code).
- **whitenoise** : Gestion simplifiée des fichiers statiques en production.

Conteneurisation et infrastructure
-----------------------------------

- **Docker** : Conteneurisation de l’application pour une portabilité maximale.
- **Docker Hub** : Registre distant pour héberger les images Docker.
- **CI/CD (GitHub Actions)** : Automatisation des tests, du build et du déploiement.
- **Hébergeur (Render, AWS ou autre)** : Exécution du projet déployé en production.

Autres outils et fichiers de configuration
------------------------------------------

- **requirements.txt** : Liste des dépendances Python.
- **.env / variables d’environnement** : Stockage sécurisé des paramètres sensibles.
- **coverage.py** : Mesure de la couverture des tests.
- **Sphinx** (optionnel) : Génération de la documentation technique.

Résumé des points forts techniques
-----------------------------------

- Architecture Django **modulaire** : séparation claire des applications (`lettings`, `profiles`)
- Pipeline **CI/CD complet** avec vérification qualité (lint), tests et déploiement automatique
- Intégration robuste de la **surveillance des erreurs**
- Déploiement Dockerisé, reproductible localement ou sur un hébergeur cloud
