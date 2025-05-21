from django.urls import reverse, resolve
from profiles import views


def test_index_url_resolves():
    path = reverse("profiles_index")
    assert resolve(path).func == views.index


def test_profile_url_resolves():
    path = reverse("profile", kwargs={"username": "testuser"})
    assert resolve(path).func == views.profile
