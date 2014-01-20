from django.db import models

# Create your models here.
class Recipe(models.Model):
 obj = models.CharField(max_length=50)
 image = models.CharField(max_length=250)
 info = models.CharField(max_length=2000)
 date = models.CharField(max_length=20)

 def __unicode__(self):
  return self.youtube

