from django.db import models
from django.utils import timezone
from seller.models import New_sup

# Create your models here.
class Discussion(models.Model):
    name = models.CharField(max_length=100)
    dis_id = models.CharField(max_length=100,unique=True,primary_key=True)
    topic = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)
    last = models.CharField(max_length=100)
    cmnt = models.IntegerField(default=0)
    last_time = models.DateTimeField(default=timezone.now)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content

class Comment(models.Model):
    name = models.CharField(max_length=100)
    dis_id = models.ForeignKey(Discussion,on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=1000)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content

