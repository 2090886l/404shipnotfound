from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    high_score = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='profile_images', blank=True) #still working on picture
    def __unicode__(self):
        return unicode(self.user.username)
        
        
class Game(models.Model):
    user = models.ForeignKey(User)
    score = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    win = models.BooleanField(default=False)
    def __unicode__(self):
        return unicode(self.date)