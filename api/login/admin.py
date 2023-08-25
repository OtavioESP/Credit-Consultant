from django.contrib import admin

from login.models import User

from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
