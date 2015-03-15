from django.shortcuts import render
from _404shipnotfound.models import Game, UserProfile



def index(request):



    return render(request, 'app/index.html')
    
def home(request):
    list = Game.objects.order_by('-score')[:10]
    if request.user.is_authenticated():
        userprofile = UserProfile.objects.get(user = request.user)
    else:
        userprofile = ""

    return render(request, 'app/home.html', {"games" : list, "profile" : userprofile})