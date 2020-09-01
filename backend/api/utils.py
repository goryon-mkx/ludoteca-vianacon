from boardgamegeek import BGGClient

from api.models import BggGame


class BggGameUtils:
    @staticmethod
    def create(bggid):
        client = BGGClient()
        game = client.game(game_id=bggid)

        bgggame = BggGame(bggid=game.id)
        bgggame.name = game.name
        bgggame.thumbnail = game.thumbnail or ""
        bgggame.image = game.image or ""
        bgggame.min_players = game.minplayers
        bgggame.max_players = game.maxplayers
        bgggame.min_playtime = game.minplaytime
        bgggame.max_playtime = game.maxplaytime
        bgggame.rank = game.boardgame_rank
        # bgggame.other_names = list(game.alternative_names)
        bgggame.save()
        return bgggame

    @staticmethod
    def find(bggid):
        return BggGame.objects.filter(pk=bggid).first()
