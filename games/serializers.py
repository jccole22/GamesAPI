from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'genre', 'description', 'release_date', 'developer', 'publisher', 'price')
        lookup_field = 'title'