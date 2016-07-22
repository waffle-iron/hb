from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from userprofile.models import HBUser

class HBUserAdmin(UserAdmin):
    pass

admin.site.register(HBUser, HBUserAdmin)