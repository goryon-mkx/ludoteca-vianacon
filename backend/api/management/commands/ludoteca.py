from _ast import keyword

import pandas as pd
from boardgamegeek import BGGClient
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from backend.api import utils
from backend.api.models import Location

User = get_user_model()

bgg = BGGClient()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file")

    def add_game(self, bggid, owners):
        for owner in owners:
            utils.Library.create(bggid, owner.strip())

    # @transaction.atomic
    def handle(self, *args, **options):
        skipped = []
        self.stdout.write(options["file"])
        table = pd.read_csv(options["file"], header=0, delimiter=";")
        for _, row in table.iterrows():
            owners = row["owners"].split(",")
            bggid = row["bggid"]
            print(f"{row}; {bggid}; {owners}")
            if bggid:
                try:
                    self.add_game(bggid, owners)
                except Exception as err:
                    # add to skip file
                    skipped.append(str(bggid) + ";" + row["owners"])

            else:
                print("game without id")
