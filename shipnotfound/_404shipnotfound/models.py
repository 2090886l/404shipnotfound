from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    high_score = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def save(self, *args, **kwargs):
        if self.high_score < 0:
            self.high_score = 0
        super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.user.username)

class Game(models.Model):
    user = models.ForeignKey(User)
    score = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    win = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.score < 0:
            self.score = 0
        super(Game, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.date)
