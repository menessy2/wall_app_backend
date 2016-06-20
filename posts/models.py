from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from accounts.models import CustomerUser
# Create your models here.




class Post(models.Model):
    creator = models.ForeignKey(CustomerUser)
    content = models.TextField()

    creation_time = models.DateTimeField(default=timezone.now)
    last_edit     = models.DateTimeField(default=timezone.now)


    def get_likes_count(self):
        return self.like_set.all().count()

    def get_creator_name(self):
        return u'%s' % self.creator.username



class Like(models.Model):

    creator = models.ForeignKey(CustomerUser)
    post    = models.ForeignKey(Post)
    creation_time = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('creator', 'post',)