import logging
from django.shortcuts import render, get_object_or_404
from profiles.models.profile import Profile

logger = logging.getLogger(__name__)


def index(request):
    """
    Vue de la liste des profils.
    """
    logger.info("Accès à la page de liste des profils")
    try:
        profiles_list = Profile.objects.all()
        context = {"profiles_list": profiles_list}
        return render(request, "profiles/index.html", context)
    except Exception as e:
        logger.error(
            "Erreur lors de l'affichage de la liste des profils : %s", e, exc_info=True
        )
        raise


def profile(request, username):
    """
    Vue de détail pour un profil utilisateur.
    """
    logger.info("Accès à la page de profil pour l'utilisateur '%s'", username)
    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {"profile": profile}
        return render(request, "profiles/profile.html", context)
    except Exception as e:
        logger.error(
            "Erreur lors de l'affichage du profil pour '%s' : %s",
            username,
            e,
            exc_info=True,
        )
        raise
