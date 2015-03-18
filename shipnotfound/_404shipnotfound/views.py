from django.shortcuts import render
from _404shipnotfound.models import Game, UserProfile



def index(request):

    return render(request, 'app/index.html')


def home(request):
    list = Game.objects.order_by('-score')[:10]
    userprofile = " "
    try:
        userprofile = UserProfile.objects.get(user = request.user.id)
    except UserProfile.DoesNotExist:
        pass

    return render(request, 'app/home.html', {"games" : list, "profile" : userprofile})


def howToPlay(request):

    return render(request, 'app/how_to_play.html')

def play(request):

    return render(request, 'app/play.html')