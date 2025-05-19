from django.shortcuts import render

def index(request):
    """
    Vue de la page d'accueil du site.

    Args:
        request (HttpRequest): La requête HTTP reçue.

    Returns:
        HttpResponse: La page HTML d'accueil.
    """
    return render(request, 'index.html')
