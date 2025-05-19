from django.contrib import admin

from lettings.models.address import Address
from lettings.models.letting import Letting
from profiles.models.profile import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
