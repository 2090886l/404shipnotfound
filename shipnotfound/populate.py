import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shipnotfound.settings')
import django
django.setup()
from _404shipnotfound.models import Game, UserProfile
from django.contrib.auth.models import User





def populate():
    # add users and games

    user1=add_player("George", "clooney", "george@gmail.com", 69)
    user2=add_player("test", "test", "test@test.com", 68)
    user3=add_player("Sam", "sammy123", "Sam@gmail.com", 29)
    user4=add_player("Bob", "thebuilder", "Bobby@yahoo.com", 56)
    user5=add_player("TheDestroyer", "42069", "destroy@kill.com", 12)

    add_game(user1, 69, True)
    add_game(user3, 29, True)
    add_game(user5, 12, True)
    add_game(user4, 0, False)
    add_game(user2, 68, True)
    add_game(user4, 56, True)
    add_game(user1, 45, True)


def add_game(user, score, win):
    g = Game.objects.get_or_create(user = user, score = score, win = win)[0]
    return g

def add_player(name, pw, email, highscore):
    try:
        user = User.objects.get(username=name)
    except:
        user = User(username=name, email=email)
        user.set_password(pw)
        user.save()
        profile = UserProfile(user=user, picture = "/static/img/default.png", high_score = highscore)
        profile.save()
    return user

# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()
