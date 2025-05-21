from django.db import models
from lettings.models.address import Address


class Letting(models.Model):
    """
    Modèle représentant une annonce de location (Letting).
    Chaque location est liée à une adresse unique.
    """

    title = models.CharField(
        max_length=256, help_text="Titre de l'annonce (ex : Appartement cosy à Paris)"
    )
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, help_text="Adresse associée à la location"
    )

    def __str__(self):
        """Retourne le titre de l'annonce."""
        return self.title

    class Meta:
        verbose_name = "Annonce"
        verbose_name_plural = "Annonces"
