from django.core.management.base import BaseCommand
from bglibrary.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        Badge.objects.all().delete()
        Player.objects.all().delete()
        BggGame.objects.all().delete()
        Game.objects.all().delete()
        LibraryGame.objects.all().delete()
        UsedGame.objects.all().delete()
        Withdraw.objects.all().delete()
