import pytest
from django.urls import reverse

from lettings.models.address import Address
from lettings.models.letting import Letting


# Testent un scénario complet, de la création à l’affichage (DB + vue + rendu)
@pytest.mark.django_db
def test_letting_full_flow(client):
    address = Address.objects.create(
        number=5,
        street="Rue Intégrée",
        city="Toulouse",
        state="OCC",
        zip_code=31000,
        country_iso_code="FR",
    )
    letting = Letting.objects.create(title="Intégration Totale", address=address)

    response_index = client.get(reverse("lettings_index"))
    assert response_index.status_code == 200
    assert "Intégration Totale" in response_index.content.decode("utf-8")

    response_detail = client.get(reverse("letting", args=[letting.id]))
    assert response_detail.status_code == 200
    assert "Rue Intégrée" in response_detail.content.decode("utf-8")


@pytest.mark.django_db
def test_letting_delete_flow(client):
    address = Address.objects.create(
        number=9,
        street="Rue à Supprimer",
        city="Lille",
        state="HDF",
        zip_code=59000,
        country_iso_code="FR",
    )
    letting = Letting.objects.create(title="À Supprimer", address=address)
    letting_id = letting.id

    letting.delete()

    response = client.get(reverse("letting", args=[letting_id]))
    assert response.status_code == 404
