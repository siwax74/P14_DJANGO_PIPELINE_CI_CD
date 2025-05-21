from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Modèle représentant le profil utilisateur personnalisé.
    Étend le modèle User par une ville favorite.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, help_text="Utilisateur associé à ce profil"
    )
    favorite_city = models.CharField(
        max_length=64,
        blank=True,
        help_text="Ville préférée de l'utilisateur (facultatif)",
    )

    def __str__(self):
        """Retourne le nom d'utilisateur lié au profil."""
        return self.user.username

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profils"
