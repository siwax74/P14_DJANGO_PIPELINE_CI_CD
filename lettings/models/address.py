from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle représentant une adresse postale complète.
    Utilisée dans l'application Lettings pour localiser un bien.
    """

    number = models.PositiveIntegerField(
        validators=[MaxValueValidator(9999)], help_text="Numéro de la voie (ex : 221)"
    )
    street = models.CharField(max_length=64, help_text="Nom de la rue")
    city = models.CharField(max_length=64, help_text="Ville")
    state = models.CharField(
        max_length=2, validators=[MinLengthValidator(2)], help_text="État (2 lettres)"
    )
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)], help_text="Code postal"
    )
    country_iso_code = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3)],
        help_text="Code ISO du pays (ex : FRA, USA)",
    )

    def __str__(self):
        """Retourne une représentation simple de l'adresse."""
        return f"{self.number} {self.street}"

    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adresses"
