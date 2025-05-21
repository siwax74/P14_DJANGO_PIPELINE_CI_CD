import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """
    Vue de la page d'accueil du site.

    Args:
        request (HttpRequest): La requête HTTP reçue.

    Returns:
        HttpResponse: La page HTML d'accueil.
    """
    logger.info("Accès à la page d'accueil (index view)")

    try:
        return render(request, "index.html")
    except Exception as e:
        logger.error(
            "Erreur lors de l'affichage de la page d'accueil : %s", e, exc_info=True
        )
        raise
