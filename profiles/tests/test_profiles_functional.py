import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models.profile import Profile


@pytest.mark.django_db
def test_index_view(client):
    user = User.objects.create(username="testuser")
    Profile.objects.create(user=user, favorite_city="testcity")

    response = client.get(reverse("profiles_index"))

    assert response.status_code == 200
    assert b"testuser" in response.content


@pytest.mark.django_db
def test_profile_view(client):
    user = User.objects.create(username="testuser")
    Profile.objects.create(user=user, favorite_city="Lyon")

    response = client.get(reverse("profile", args=["testuser"]))

    assert response.status_code == 200
    assert b"testuser" in response.content
    assert b"Lyon" in response.content


@pytest.mark.django_db
def test_profile_not_found(client):
    response = client.get(reverse("profile", args=["inconnu"]))
    assert response.status_code == 404
