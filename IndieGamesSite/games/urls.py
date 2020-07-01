from django.urls import path
from .views import GamesListView, GameDetailView


urlpatterns = [
    path('', GamesListView.as_view(), name="games"),
    path('<int:pk>', GameDetailView.as_view(), name="game_detail"),
]