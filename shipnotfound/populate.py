import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shipnotfound.settings')
import time

import django
django.setup()

from _404shipnotfound.models import Game


def populate():
    test = add_game(user = "test12", score = 12)
    time.sleep(2)

    # Print out what we have added to the user.
    for c in Game.objects.all():
            print c.date

def add_game(user, score):
    g = Game.objects.get_or_create(user = user, score = score)[0]
    return g



# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()
