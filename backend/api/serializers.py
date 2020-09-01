from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import LibraryGame, BggGame, Withdraw, Player, Badge


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = (
            'label',
        )


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'email')
        extra_kwargs = {
            'url': {'view_name': 'players', 'lookup_field': 'id'},
            'name': {'required': True},
            'email': {'required': True}
        }


class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = ('id', 'requisitor', 'game', 'date_withdrawn', 'date_returned')


class BggGameSerializer(serializers.ModelSerializer):
    badges = BadgeSerializer(many=True)

    class Meta:
        model = BggGame
        fields = (
            'bggid',
            'name',
            'rank',
            'thumbnail',
            'image',
            'min_playtime',
            'max_playtime',
            'min_players',
            'max_players',
            'badges'
        )


class LibraryGameSerializer(serializers.ModelSerializer):
    game = BggGameSerializer(read_only=True)
    owner = PlayerSerializer(read_only=True)

    game_id = serializers.IntegerField(write_only=True, required=True)
    owner_id = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all(), source="owner", required=True, write_only=True)

    currentwithdraw = SerializerMethodField()

    class Meta:
        model = LibraryGame
        fields = (
            'id',
            'game',
            'game_id',
            'owner',
            'owner_id',
            'notes',
            'location',
            'checkedin',
            'available',
            'currentwithdraw'
        )

    def get_currentwithdraw(self, obj):
        if not obj.available():
            # return WithdrawSerializer(data=obj.currentwithdraw())
            return None
        else:
            return None
