from django.contrib import admin
from django.urls import path, include

from oc_lettings_site import tests
from . import views

def sentry_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
    path("500/", tests.test_500),
    path('sentry-debug/', sentry_error),
]

