import pytest
from django.contrib.auth.models import User
from profiles.models.profile import Profile

@pytest.mark.django_db
def test_profile_str():
    user = User.objects.create(username="testuser")
    profile = Profile.objects.create(user=user, favorite_city="Paris")
    assert str(profile) == "testuser"
