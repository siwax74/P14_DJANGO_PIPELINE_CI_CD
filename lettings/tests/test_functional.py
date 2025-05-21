from django.urls import reverse
import pytest

from lettings.models.address import Address
from lettings.models.letting import Letting


# Testent le rendu d’une page HTML via requête HTTP avec client.get
@pytest.mark.django_db
def test_index_view(client):
    address = Address.objects.create(
        number=1,
        street="Rue Fonctionnelle",
        city="Nice",
        state="PACA",
        zip_code=6000,
        country_iso_code="FR",
    )
    Letting.objects.create(title="Location Fonctionnelle", address=address)

    response = client.get(reverse("lettings_index"))
    assert response.status_code == 200
    assert b"Location Fonctionnelle" in response.content


@pytest.mark.django_db
def test_letting_view(client):
    address = Address.objects.create(
        number=2,
        street="Boulevard Fonctionnel",
        city="Bordeaux",
        state="NAQ",
        zip_code=33000,
        country_iso_code="FR",
    )
    letting = Letting.objects.create(title="Letting Vue", address=address)

    response = client.get(reverse("letting", args=[letting.id]))
    assert response.status_code == 200
    assert b"Letting Vue" in response.content
    assert b"Boulevard Fonctionnel" in response.content


@pytest.mark.django_db
def test_letting_not_found(client):
    response = client.get(reverse("letting", args=[999]))
    assert response.status_code == 404
