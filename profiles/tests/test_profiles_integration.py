import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models.profile import Profile


@pytest.mark.django_db
def test_profiles_integration_flow(client):
    user = User.objects.create(username="integrationuser")
    Profile.objects.create(user=user, favorite_city="Marseille")

    response_index = client.get(reverse("profiles_index"))
    assert response_index.status_code == 200
    assert b"integrationuser" in response_index.content

    response_detail = client.get(reverse("profile", args=["integrationuser"]))
    assert response_detail.status_code == 200
    assert b"integrationuser" in response_detail.content
    assert b"Marseille" in response_detail.content


@pytest.mark.django_db
def test_profile_delete_flow(client):
    user = User.objects.create(username="deleteuser")
    profile = Profile.objects.create(user=user, favorite_city="Toulouse")

    response_index = client.get(reverse("profiles_index"))
    assert response_index.status_code == 200
    assert b"deleteuser" in response_index.content

    response_detail = client.get(reverse("profile", args=["deleteuser"]))
    assert response_detail.status_code == 200
    assert b"Toulouse" in response_detail.content

    profile.delete()

    response = client.get(reverse("profile", args=["deleteuser"]))
    assert response.status_code == 404
