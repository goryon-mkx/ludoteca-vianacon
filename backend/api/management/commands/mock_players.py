import pandas as pd
from django.core.management.base import BaseCommand

from backend.api.models import Player


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file')

    def handle(self, *args, **options):

        self.stdout.write(options['file'])
        table = pd.read_csv(options['file'], header=0, delimiter=';')
        for _, row in table.iterrows():
            player = Player()
            player.name = row['name']
            player.email = row['email']
            player.username = row['username']

            player.save()
