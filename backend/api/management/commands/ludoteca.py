from _ast import keyword
import time

import pandas as pd
from boardgamegeek import BGGClient
from boardgamegeek import exceptions as bgg_exceptions
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction


from backend.api.models import BggGame, LibraryGame
from backend.api.models import Location

User = get_user_model()

bgg = BGGClient()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file")

    def add_game(self, bggid, owners):
        try: 
            print("add_game", bggid, owners)
            for owner in owners:
                print("pre library.create", bggid, owners)
                Library.create(bggid, owner.strip())
        except Exception as e:
            print(e)

    # @transaction.atomic
    def handle(self, *args, **options):
        skipped = []
        self.stdout.write(options["file"])
        table = pd.read_csv(options["file"], header=0, delimiter=";")
        for _, row in table.iterrows():
            owners = row["owners"].split(",")
            bggid = row["bggid"]

            if bggid:
                try:
                    self.add_game(bggid, owners)
                except Exception as err:
                    # add to skip file
                    skipped.append(str(bggid) + ";" + row["owners"])

            else:
                print("game without id")


class Player:
    @staticmethod
    def create_player(username):
        player = User()
        player.username = username
        player.email = username + "@" + "dumbmail.com"
        player.first_name = username
        player.save()
        return player


class Library:
    @staticmethod
    def create(bgg_id, owner):
        search = BggGame.objects.filter(bggid=bgg_id)
        if search.count():
            bgg_game = search.first()
        else:

            response = BoardGameGeek.get_external_game(bgg_id)

            bgg_game = BGGGame.create(response.id)

        if bgg_game:
            playersfilter = User.objects.filter(username=owner)

            if playersfilter.count():
                player = playersfilter.first()
            else:
                player = Player.create_player(owner)

            game = LibraryGame(game=bgg_game, owner=player)

            game.game = bgg_game

            game.save()
        else:
            print("game not found (" + str(bgg_id) + ")")


class BGGGame:
    @staticmethod
    def create(bgg_id):
        client = BGGClient()
        game = BoardGameGeek.get_external_game(bgg_id)

        bgg_game = BggGame(bggid=game.id)
        bgg_game = BoardGameGeek.convert_external_game(external=game, game=bgg_game)
        bgg_game.save()
        return bgg_game

    @staticmethod
    def find(bgg_id):
        return BggGame.objects.filter(pk=bgg_id).first()


class BoardGameGeek:
    @staticmethod
    def convert_external_game(external, game):
        game.name = external.name
        game.thumbnail = external.thumbnail or ""
        game.image = external.image or ""
        game.min_players = external.minplayers
        game.max_players = external.maxplayers
        game.min_playtime = external.minplaytime
        game.max_playtime = external.maxplaytime
        game.rank = external.boardgame_rank
        game.weight = external.rating_average_weight or 0
        game.other_names = external.alternative_names
        game.year = external.yearpublished or 0
        return game

    @staticmethod
    def get_external_game(bgg_id):
        bgg = BGGClient()
        max_count = 10
        while max_count:
            try:
                return bgg.game(game_id=bgg_id)

            except bgg_exceptions.BGGValueError:
                print("[ERROR] Invalid parameters")
                raise

            except bgg_exceptions.BGGApiRetryError:
                print("[ERROR] Retry after delay, retrying...")
                BoardGameGeek._retry(max_count)

            except bgg_exceptions.BGGApiError:
                print("[ERROR] API response invalid or not parsed")
                BoardGameGeek._retry(max_count)

            except bgg_exceptions.BGGApiTimeoutError:
                print("[ERROR] Timeout")
                BoardGameGeek._retry(max_count)

            except Exception as err:
                print("[ERROR] Exception caught getting external game: " + str(err))
                BoardGameGeek._retry(max_count)

        raise Exception

    @staticmethod
    def _retry(count):
        count -= 1
        time.sleep(1)