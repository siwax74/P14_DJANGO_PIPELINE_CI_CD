Description du projet
=====================

Présentation générale
---------------------

Ce projet est un site web de location immobilière basé sur le framework **Django**.  
Il permet d’afficher des profils d’utilisateurs ainsi que des offres de locations disponibles.

Le but principal de ce projet est d’illustrer une architecture Django modulaire, évolutive, maintenable et conforme aux bonnes pratiques de développement logiciel. Il inclut également une couverture de tests élevée, une gestion des erreurs via Sentry, une intégration CI/CD complète, et une documentation technique rigoureuse.

Objectifs du projet
-------------------

- Refactorisation d’une architecture Django monolithique en structure modulaire.
- Séparation des fonctionnalités en applications indépendantes : ``lettings`` et ``profiles``.
- Maintien de l’apparence et des fonctionnalités existantes (refactorisation pure).
- Intégration de la gestion d’erreurs avancée avec **Sentry**.
- Ajout de logs structurés via le module ``logging``.
- Mise en place d’un pipeline **CI/CD** pour les tests, la conteneurisation et le déploiement.
- Création d’une documentation technique complète et claire.

Fonctionnalités principales
---------------------------

- Page d’accueil avec redirection vers les modules.
- Module **Lettings** :
  - Affichage des locations disponibles
  - Détails des adresses
- Module **Profiles** :
  - Affichage des profils d’utilisateurs
- Interface d'administration Django entièrement fonctionnelle
- Gestion des erreurs personnalisées (pages 404 et 500)
- Suivi des erreurs critiques via **Sentry**
- Tests unitaires et d’intégration (>80% de couverture)
- Linting conforme avec ``flake8``

Public cible
------------

Ce projet est destiné à :

- Des développeurs ou équipes souhaitant un exemple concret d’un projet Django bien structuré.
- Des équipes DevOps souhaitant intégrer un workflow CI/CD complet.
- Des recruteurs ou formateurs cherchant un support pédagogique pour illustrer les bonnes pratiques Django.

