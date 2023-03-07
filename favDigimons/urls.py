from django.urls import path
from .views import FavoriteListView,FavoriteDetailView

urlpatterns = [
    path('',FavoriteListView.as_view(), name='favorite_list'),
    path('<int:pk>/', FavoriteDetailView.as_view(), name='favorite_detail'),
]