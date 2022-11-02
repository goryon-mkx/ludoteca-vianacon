from django.db.models import Avg, Count, ExpressionWrapper, F, Sum, fields
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.api.models import LibraryGame, StoreGame, Withdraw
from backend.api.views.games import User


class StatisticsViewSet(APIView):
    def get(self, request):
        return Response(
            {
                "library": self._load_library_statistics(),
                "store": self._load_store_statistics(),
            }
        )

    def _load_library_statistics(self):
        # Load users ordered by number of withdraws
        users = [
            {
                "id": user.id,
                "name": f"{user.first_name} {user.last_name}",
                "count": user.num_withdraws,
            }
            for user in User.objects.annotate(num_withdraws=Count("withdraw")).order_by(
                "-num_withdraws"
            )
        ][:5]

        # Load games order by number of withdraws
        all_popular_games = LibraryGame.objects.annotate(
            num_withdraws=Count("withdraw")
        ).order_by("-num_withdraws")

        ongoing_withdraws = Withdraw.objects.filter(
            date_returned__isnull=True
        ).aggregate(
            min_players=Sum("game__game__min_players"),
            max_players=Sum("game__game__max_players"),
            total=Count("*"),
        )

        duration = ExpressionWrapper(
            F("date_returned") - F("date_withdrawn"),
            output_field=fields.DurationField(),
        )
        average_duration = (
            Withdraw.objects.annotate(duration=duration)
            .filter(date_returned__isnull=False)
            .aggregate(average=Avg(duration))
        )

        popular_games = [
            {
                "id": game.id,
                "bggid": game.game.bggid,
                "game": f"{game.game.name}",
                "requisitions": game.num_withdraws,
            }
            for game in all_popular_games[:5]
        ]

        return {
            "games": {
                "total": LibraryGame.objects.all().count(),
                "being_played": ongoing_withdraws.get("total"),
                "not_checked_in": LibraryGame.objects.filter(
                    location__isnull=True
                ).count(),
            },
            "requisitors": {
                "total": User.objects.all().count(),
            },
            "withdraws": {
                "total": Withdraw.objects.all().count(),
                "recent": {
                    "out": [
                        {
                            "game_id": w.game_id,
                            "bggid": w.game.game.bggid,
                            "game": w.game.game.name,
                            "image": w.game.game.image,
                            "date": w.date_withdrawn,
                        }
                        for w in Withdraw.objects.all().order_by("-date_withdrawn")[:8]
                    ],
                    "in": [
                        {
                            "game_id": w.game_id,
                            "bggid": w.game.game.bggid,
                            "image": w.game.game.image,
                            "game": w.game.game.name,
                            "date": w.date_returned,
                        }
                        for w in Withdraw.objects.all().order_by("-date_returned")[:8]
                    ],
                },
                "popular": {"requisitors": users, "games": popular_games},
                "players": {
                    "min_players": ongoing_withdraws.get("min_players"),
                    "max_players": ongoing_withdraws.get("max_players"),
                },
                "duration": average_duration,
            },
        }

    def _load_store_statistics(self):
        return {
            "total": StoreGame.objects.all().count(),
            "available": StoreGame.objects.filter(stock__gte=0).count(),
        }
