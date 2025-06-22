Guide d'utilisation
===================

Vue d'ensemble
--------------

L’application est composée de deux modules fonctionnels principaux :

- **Lettings** : gestion et visualisation des offres de locations.
- **Profiles** : visualisation des profils d’utilisateurs associés aux locations.

Le site s’adresse à un public général qui souhaite consulter des offres de logement, ainsi qu’à des administrateurs qui peuvent gérer le contenu via l’interface d’administration Django.

Accès au site
-------------

- **Page d’accueil** : http://127.0.0.1:8000  
  Permet d’accéder aux modules Lettings et Profiles.

- **Interface d'administration** : http://127.0.0.1:8000/admin  
  Accessible uniquement après authentification avec un compte superutilisateur.

Cas d’utilisation
------------------

1. **Naviguer dans les offres de location**

   - Depuis la page d’accueil, cliquez sur "Lettings".
   - Une liste de logements s'affiche avec leur titre.
   - Cliquez sur un logement pour afficher ses détails (adresse, code postal, etc.).

2. **Consulter les profils utilisateurs**

   - Depuis la page d’accueil, cliquez sur "Profiles".
   - Vous verrez la liste des profils enregistrés.
   - Cliquez sur un nom pour consulter les détails du profil (préférence de langue, description, etc.).

3. **Utiliser l’interface d’administration**

   - Accédez à `/admin` et connectez-vous avec un compte superutilisateur.
   - Gérez les modèles : `Letting`, `Address`, `Profile`, `User`...
   - Ajoutez, modifiez ou supprimez des entrées.
   - Visualisez la liste des objets avec leurs champs.

4. **Pages d’erreur personnalisées**

   - Si vous accédez à une page inexistante, une page 404 personnalisée s’affiche.
   - En cas d’erreur serveur, une page 500 dédiée est également rendue.

Raccourcis de navigation
-------------------------

- **Accueil** : `/`
- **Locations** : `/lettings/`
- **Détails location** : `/lettings/<id>/`
- **Profils** : `/profiles/`
- **Détails profil** : `/profiles/<username>/`

Accès administrateur requis
---------------------------

L’administration nécessite :

- un compte superutilisateur (créé via `createsuperuser`)
- une connexion pour accéder à l’interface Django admin

