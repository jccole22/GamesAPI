from django.shortcuts import render
from rest_framework import viewsets
from .models import Game
from .serializers import GameSerializer

class GameView(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
