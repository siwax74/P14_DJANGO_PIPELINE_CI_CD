from django.contrib import admin
from django.urls import path, include

from oc_lettings_site import tests
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('500/', tests.test_500),
] 
