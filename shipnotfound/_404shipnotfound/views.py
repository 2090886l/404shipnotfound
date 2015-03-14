from django.shortcuts import render
from _404shipnotfound.models import Game



def index(request):



    return render(request, 'app/index.html', {"games" : list})
    
def home(request):


    list = Game.objects.order_by('-score')[:10]


    return render(request, 'app/home.html', {"games" : list})