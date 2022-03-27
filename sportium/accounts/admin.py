from django.contrib import admin

from sportium.accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
    # list_display = ('first_name', 'last_name')
