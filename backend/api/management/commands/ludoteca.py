import calendar
import logging
import time
from datetime import datetime

import boardgamegeek
import pandas as pd
from boardgamegeek import BGGClient
from django.core.management.base import BaseCommand

from api import utils
from api.models import BggGame, LibraryGame, Player
from api.utils import BggGameUtils

bgg = BGGClient()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file')

    def find(self, query):
        max_count = 10
        print(' -- Fetching game with id: '+str(query))
        while max_count:
            try:
                rs = bgg.search(query)

                if rs:
                    return bgg.game(game_id=rs[0].id)

            except boardgamegeek.exceptions.BGGValueError as err:
                print('[ERROR] Invalid parameters')
                max_count = 0

            except boardgamegeek.exceptions.BGGApiRetryError:
                print('[ERROR] Retry after delay')
                max_count -= 1
                time.sleep(10)

            except boardgamegeek.exceptions.BGGApiError:
                print('[ERROR] API response invalid or not parsed')
                max_count = 0

            except boardgamegeek.exceptions.BGGApiTimeoutError:
                print('[ERROR] Timeout')
                max_count -= 1
                time.sleep(10)

            except Exception as err:
                print('err')
                max_count -= 1
                time.sleep(10)

        return None

    def create_bgg(self, game):
        # bgggame = BggGame(bggid=game.id)
        # bgggame.name = game.name
        # bgggame.thumbnail = game.thumbnail or ""
        # bgggame.image = game.image or ""
        # bgggame.min_players = game.min_players
        # bgggame.max_players = game.max_players
        # bgggame.min_playtime = game.minplaytime
        # bgggame.max_playtime = game.maxplaytime
        # bgggame.rank = game.boardgame_rank
        # bgggame.other_names = str(game.alternative_names)
        # bgggame.save()
        # return bgggame
        return BggGameUtils.create(game.id)

    def create_player(self, username):
        player = Player()
        player.username = username
        player.email = username + '@' + 'dumbmail.com'
        player.name = username
        player.save()
        return player

    def add_game(self, bggid, owners):
        for owner in owners:
            self.add_game_to_owner(bggid, owner.strip())

    def add_game_to_owner(self, bggid, owner):
        search = BggGame.objects.filter(bggid=bggid)
        if search.count():
            bgggame = search.first()
        else:
            response = self.find(bggid)
            bgggame = self.create_bgg(response)

        if bgggame:
            playersfilter = Player.objects.filter(username=owner)

            if playersfilter.count():
                player = playersfilter.first()
            else:
                player = self.create_player(owner)

            game = LibraryGame(game=bgggame, owner=player)

            game.game = bgggame

            game.save()
        else:
            print('game not found (' + str(bggid) + ')')

    def handle(self, *args, **options):
        self.stdout.write(options['file'])
        table = pd.read_csv(options['file'], header=0, delimiter=';')
        for _, row in table.iterrows():
            owners = row['owners'].split(",")
            bggid = row['bggid']
            if bggid:
                self.add_game(bggid, owners)
            else:
                print('game without id')
