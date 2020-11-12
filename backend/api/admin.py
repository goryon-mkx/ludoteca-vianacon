from django.contrib import admin

# Register your models here.
from backend.api.models import BggGame, Badge


@admin.register(BggGame)
class BggGameAdmin(admin.ModelAdmin):
    fields = ('name', 'bggid', 'badges',)
    readonly_fields = ('bggid', 'name',)
    ordering = ('name',)


admin.site.register(Badge)
