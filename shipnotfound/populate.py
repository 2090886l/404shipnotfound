import os
import time
import django
from _404shipnotfound.models import Game, UserProfile
from django.contrib.auth.models import User
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shipnotfound.settings')
django.setup()




def populate():
    # add users and games
    
    user1=add_player("George", "clooney", "george@gmail.com")
	user2=add_player("test", "test", "test@test.com")
	user3=add_player("Sam", "sammy123", "Sam@gmail.com")
	user4=add_player("Bob", "thebuilder", "Bobby@yahoo.com")
	user5=add_player("TheDestroyer", "42069", "destroy@kill.com")
    
    game1=add_game(user1, 69, True)
    game2=add_game(user3, 29, True)
    game3=add_game(user5, 12, True)
    game4=add_game(user4, 0, False)
    game5=add_game(user2, 68, True)
    game6=add_game(user4, 56, True)
    game7=add_game(user1, 45, True)
    

def add_game(user, score, win):
    g = Game.objects.get_or_create(user = user, score = score)[0]
    return g

def add_player(name, pw, email):
    try:
        user = User.objects.get(username=name)
    except:
        user = User(username=name, email=email)
        user.set_password(pw)
        user.save()
        profile = UserProfile(user=user)
        profile.save()
    return u

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()
