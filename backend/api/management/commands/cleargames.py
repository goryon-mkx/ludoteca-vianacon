from django.core.management.base import BaseCommand

from backend.api.models import LibraryGame


class Command(BaseCommand):

    def handle(self, *args, **options):
        for g in LibraryGame.objects.all():
            g.delete()
