from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from _404shipnotfound.models import Game, UserProfile

# method to add games
def add_game(username, score, win):
    g = Game.objects.get_or_create(user=username)[0]
    g.score = score
    g.win = win
    g.save()
    return g

# method to add users
def add_user(username, high_score):
    u = Game.objects.get_or_create(user=username)[0]
    u.high_score = high_score
    u.save()
    return u

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

    # tests if high score board updates
    def test_home_view_with_games(self):

        # add games
        add_game(User.objects.create_user(username='test1', email='test@test.com', password='top_secret'),100,1)
        add_game(User.objects.create_user(username='test2', email='test@test.com', password='top_secret'),12,1)
        add_game(User.objects.create_user(username='user', email='test@test.com', password='top_secret'),13,1)
        add_game(User.objects.create_user(username='user_test', email='test@test.com', password='top_secret'),13,1)

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        # checks if games show in high score board
        self.assertContains(response, "user_test")

        num_games =len(response.context['games'])
        self.assertEqual(num_games , 4)

class IndexViewTests(TestCase):

    # test view opens
    def test_index_view_works(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class ProfileViewTests(TestCase):

    # If no user exist, an appropriate message should be displayed.
    def test_profile_view_no_user(self):
        response = self.client.get('http://127.0.0.1:8000/profile/random/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User does not exist!")

    # test profile page works
    def test_profile_view_works(self):
        add_user(User.objects.create_user(username='Greg', email='Greg@test.com', password='top_secret'), 70)
        response = self.client.get('http://127.0.0.1:8000/profile/Greg/')
        # checks that it opens
        self.assertEqual(response.status_code, 200)
        # checks that the username shows
        self.assertContains(response, "Greg")
