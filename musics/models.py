from django.db import models


class Music(models.Model):
 artist = models.CharField(max_length=50)
 song = models.CharField(max_length=50)
 year = models.IntegerField()

 def __unicode__(self):
  return self.artist


