from django.shortcuts import render, get_object_or_404
from lettings.models.letting import Letting


def index(request):
    """
    Vue pour la page d’index des locations.
    Affiche la liste de toutes les annonces.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Vue pour afficher les détails d’une location spécifique.
    
    Args:
        request: Objet HttpRequest.
        letting_id (int): ID de la location à afficher.

    Returns:
        HttpResponse: Page de détails avec le titre et l’adresse.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
