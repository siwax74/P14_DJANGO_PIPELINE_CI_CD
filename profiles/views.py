from django.shortcuts import render, get_object_or_404
from profiles.models.profile import Profile

def index(request):
    """
    Vue de la liste des profils.

    Affiche tous les profils disponibles.

    Args:
        request (HttpRequest): La requête HTTP reçue.

    Returns:
        HttpResponse: La page HTML contenant la liste des profils.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Vue de détail pour un profil utilisateur.

    Args:
        request (HttpRequest): La requête HTTP reçue.
        username (str): Le nom d'utilisateur associé au profil.

    Returns:
        HttpResponse: La page HTML contenant les détails du profil.
        Http404: Si le profil n'existe pas.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
