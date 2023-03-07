from django.shortcuts import render
from .models import Digimon
from .serializers import DigimonSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.

class FavoriteListView(ListCreateAPIView):
    queryset=Digimon.objects.all()
    serializer_class=DigimonSerializer

class FavoriteDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Digimon.objects.all()
    serializer_class=DigimonSerializer