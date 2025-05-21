from django.urls import reverse, resolve
from lettings import views


def test_index_url_resolves():
    path = reverse("lettings_index")
    assert resolve(path).func == views.index


def test_letting_url_resolves():
    path = reverse("letting", kwargs={"letting_id": 1})
    assert resolve(path).func == views.letting
