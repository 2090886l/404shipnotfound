from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from _404shipnotfound.models import Game, UserProfile

class GameMethodTests(TestCase):

    # ensure_scores_are_positive should results True for games where scores are zero or positive
    def test_ensure_scores_are_positive(self):
        game = Game(user = User.objects.create_user(username='test', email='test@test.com', password='top_secret'), score = -1)
        game.save()
        self.assertEqual((game.score >= 0), True)

class UserProfileMethodTests(TestCase):

    # ensure_high_scores_are_positive should results True for userProfiles where high scores are zero or positive
    def test_ensure_high_scores_are_positive(self):
        u = UserProfile(user = User.objects.create_user(username='test', email='test@test.com', password='top_secret'), high_score = -1)
        u.save()
        self.assertEqual((u.high_score >= 0), True)


class HomeViewTests(TestCase):

    # test view opens
    def test_home_view_works(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class IndexViewTests(TestCase):

    # test view opens
    def test_index_view_works(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class PlayViewTests(TestCase):

    # test view opens
    def test_play_view_works(self):
        response = self.client.get(reverse('play'))
        self.assertEqual(response.status_code, 200)
