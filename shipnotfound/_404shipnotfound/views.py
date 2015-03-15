from django.shortcuts import render
from _404shipnotfound.models import Game, UserProfile



def index(request):



    return render(request, 'app/index.html')
    
def home(request):


    list = Game.objects.order_by('-score')[:10]
    userprofile = UserProfile.objects.get(user = request.user)


    return render(request, 'app/home.html', {"games" : list, "profile" : userprofile})