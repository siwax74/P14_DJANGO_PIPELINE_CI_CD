import logging
from django.shortcuts import render, get_object_or_404
from lettings.models.letting import Letting

logger = logging.getLogger(__name__)


def index(request):
    """
    Vue pour la page d’index des locations.
    Affiche la liste de toutes les annonces.
    """
    logger.info("Accès à la page de liste des locations")
    try:
        lettings_list = Letting.objects.all()
        context = {"lettings_list": lettings_list}
        return render(request, "lettings/index.html", context)
    except Exception as e:
        logger.error(
            "Erreur lors de l'affichage de la page des locations : %s", e, exc_info=True
        )
        raise


def letting(request, letting_id):
    """
    Vue pour afficher les détails d’une location spécifique.
    """
    logger.info("Accès à la page de détail de la location ID=%s", letting_id)
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "lettings/letting.html", context)
    except Exception as e:
        logger.error(
            "Erreur lors de l'affichage de la location ID=%s : %s",
            letting_id,
            e,
            exc_info=True,
        )
        raise
