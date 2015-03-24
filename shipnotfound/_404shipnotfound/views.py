from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from _404shipnotfound.models import Game, UserProfile
from _404shipnotfound.forms import UserProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def register_profile(request):
    context_dict = {}
    registered = False
    if request.method == 'POST':
        
        try:
            profile = UserProfile.objects.get(user=request.user)
            profile_form = UserProfileForm(request.POST, instance=profile)
        except:
            profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']  
            profile.save()
            registered = True
        else:
            print profile_form.errors
    else:
        UserProfile.objects.get_or_create(user = request.user, high_score = 0, picture = "/static/img/ship.jpg")
        profile_form = UserProfileForm() 
    context_dict['profile_form'] = profile_form
    context_dict['registered'] = registered
    
    return render(request, 'registration/profile_registration.html', context_dict)

	
def index(request):

    return render(request, 'app/index.html')


def home(request):
    list = Game.objects.order_by('-score')[:10]
    userprofile = " "
    games = 0
    wins = 0
    losses = 0
    high_score = 0
    max_date = "No games played yet."
    if request.user.is_authenticated():

        try:
            userprofile = UserProfile.objects.get(user = request.user.id)
            high_score = userprofile.high_score
        except UserProfile.DoesNotExist:
            pass
        
        flag = True;
        for game in Game.objects.all():

            if request.user == game.user:
                if flag:
                    max_date = game.date
                    flag = False
                if game.date > max_date:
                    max_date = game.date               
                if game.win == True:
                    wins = wins + 1
                else:
                    losses = losses + 1
                games = games + 1

        return render(request, 'app/home.html', {"games" : list, "profile" : userprofile, "games_played" : games, "wins" : wins, "losses" : losses, "last_played": max_date, "high_score": high_score})
    
    return render(request, 'app/home.html')
    
def howToPlay(request):

    return render(request, 'app/how_to_play.html')

def play(request, difficulty):

    return render(request, 'app/play.html', {"difficulty" : difficulty})
    
    
def record(request, type, score):

    if request.user.is_authenticated():
        try:       
            if type == "1":
                Game.objects.create(user = request.user, score = score, win = True)
            else:
                Game.objects.create(user = request.user, score = score, win = False)
        except Game.DoesNotExist:
            pass

        try:
            userprofile = UserProfile.objects.get(user = request.user)
            if int(score) > userprofile.high_score:
                userprofile.high_score = score
                userprofile.save()
                
        except UserProfile.DoesNotExist:
            pass
    return HttpResponseRedirect('/home')
    
# @login_required  
# def win(request):

    # return render(request, 'app/play.html')    
