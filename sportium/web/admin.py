from django.contrib import admin

from sportium.web.models import Club, Player


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass
    # list_display = ('first_name', 'last_name')
