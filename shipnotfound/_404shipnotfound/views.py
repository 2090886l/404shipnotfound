from django.shortcuts import render
from _404shipnotfound.models import Game, UserProfile



def index(request):

    return render(request, 'app/index.html')


def home(request):
    list = Game.objects.order_by('-score')[:10]
    userprofile = " "
    games = 0
    wins = 0
    losses = 0

    try:
        userprofile = UserProfile.objects.get(user = request.user.id)
    except UserProfile.DoesNotExist:
        pass

    for game in Game.objects.all():
        if game.win == True:
            wins = wins + 1
        else:
            losses = losses + 1
        games = games + 1

    return render(request, 'app/home.html', {"games" : list, "profile" : userprofile, "games_played" : games, "wins" : wins, "losses" : losses})


def howToPlay(request):

    return render(request, 'app/how_to_play.html')

def play(request):

    return render(request, 'app/play.html')