from boardgamegeek import BGGClient
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from backend.api import utils
from backend.api.models import BggGame
from backend.api.utils import BoardGameGeek

User = get_user_model()

bgg = BGGClient()


class Command(BaseCommand):
    def handle(self, *args, **options):
        for game in BggGame.objects.filter(year=""):
            external_game = utils.BoardGameGeek.get_external_game(game.bggid)
            game = utils.BoardGameGeek.convert_external_game(external_game, game)
            game.save()
