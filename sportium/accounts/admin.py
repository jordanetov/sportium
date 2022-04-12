from django.contrib import admin

from sportium.accounts.models import Profile
from sportium.common.helpers import UserModel


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
    # list_display = ('first_name', 'last_name')


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    pass
