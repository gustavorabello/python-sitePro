from django.db import models

class Image(models.Model):
 filename = models.CharField(max_length=50)
 dimension = models.CharField(max_length=3)
 date = models.CharField(max_length=12)
 text = models.CharField(max_length=5000)

 def __unicode__(self):
  return self.abstract

