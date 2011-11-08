from django.db import models

# Create your models here.
class Video(models.Model):
 filename = models.CharField(max_length=50)
 title = models.CharField(max_length=50)
 youtube = models.CharField(max_length=250)
 description = models.CharField(max_length=2000)

 def __unicode__(self):
  return self.youtube

