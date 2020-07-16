from django.shortcuts import render
from games.models import Game
# from ..games.models import Game

# Create your views here.
def index(request):
    recent_games = Game.objects.filter().order_by('pub_date')[:4]
    context = {'recent_games': recent_games}
    return render(request, 'core/index.html', context)

def error_404_view(request, exception):
    return render(request, '404.html', status=404)
