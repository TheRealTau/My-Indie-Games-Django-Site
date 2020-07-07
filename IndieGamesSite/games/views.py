from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Game
from taggit.models import Tag


# Create your views here.
class GamesListView(ListView):
    model = Game
    template_name = 'games/games_list.html'
    paginate_by = 4
    context_object_name = 'games'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = Game.objects.all()

        return context

class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game_detail.html'

    def get_object(self):
        return get_object_or_404(Game, pk=self.kwargs['pk'])

class TaggedListView(ListView):
    model = Game
    template_name = 'games/tagged_games_list.html'
    paginate_by = 4
    context_object_name = 'tagged_games'
    # tag = None

    def get_context_data(self, **kwargs):
        tag = get_object_or_404(Tag, slug=self.kwargs['tag_name'].lower())
        games = Game.objects.filter(tags=tag)
        context = super().get_context_data(**kwargs)
        context['games'] = games
        context['tag'] = tag
        return context
