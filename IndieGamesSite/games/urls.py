from django.urls import path
from .views import GamesListView, GameDetailView, TaggedListView


urlpatterns = [
    path('', GamesListView.as_view(), name="games"),
    path('<int:pk>', GameDetailView.as_view(), name="game_detail"),
    path('tagged/<slug:tag_name>', TaggedListView.as_view(), name="tagged_games"),
]
