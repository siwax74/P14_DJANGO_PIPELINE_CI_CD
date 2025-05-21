import pytest

from lettings.models.address import Address
from lettings.models.letting import Letting


@pytest.mark.django_db
def test_letting_str():
    address = Address.objects.create(
        number=10,
        street="Rue Unitaire",
        city="Paris",
        state="IDF",
        zip_code=75001,
        country_iso_code="FR",
    )
    letting = Letting.objects.create(title="Test Letting", address=address)
    assert str(letting) == "Test Letting"


@pytest.mark.django_db
def test_address_str():
    address = Address.objects.create(
        number=20,
        street="Avenue Unitaire",
        city="Lyon",
        state="ARA",
        zip_code=69000,
        country_iso_code="FR",
    )
    assert str(address) == "20 Avenue Unitaire"
