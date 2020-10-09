
import random


from boardgamegeek import BGGClient
from django.core.management.base import BaseCommand
from django.utils import timezone

from backend.api.models import LibraryGame, Withdraw, Player

bgg = BGGClient()


class Command(BaseCommand):

    def handle(self, *args, **options):
        shelves = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2',
                   'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5']

        statuses = ['not-checkedin', 'available', 'not-available', 'checkedout']

        for game in LibraryGame.objects.all():
            # understand wich it will be the status of the mocked game
            # 0 => not checkedin,
            # 1 => available
            # 2 => on the table
            # 3 => checkedout
            mode = random.randint(0, 99)
            # mode = random.choice(statuses)

            if 0 <= mode < 5:
                game.location = ''
                game.date_checkout = None

            elif 5 <= mode < 85:
                game.location = random.choice(shelves)
                withdraw_filter = game.withdraw_set.filter(date_returned=None)
                if withdraw_filter.count() > 0:
                    for w in withdraw_filter:
                        w.date_returned = timezone.now()
                        w.save()

            elif 85 <= mode < 99:
                game.location = random.choice(shelves)
                withdraw = Withdraw()
                withdraw.game = game
                withdraw.requisitor = random.choice(Player.objects.all())
                withdraw.date_withdrawn = timezone.now()
                withdraw.save()

            elif mode >= 7:
                game.location = ''
                game.date_checkout = timezone.now()

            game.save()
