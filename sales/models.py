from django.db import models

# Create your models here.
class Sale(models.Model):
 obj = models.CharField(max_length=50)
 image = models.CharField(max_length=250)
 link = models.CharField(max_length=2000)
 info = models.CharField(max_length=2000)
 original = models.CharField(max_length=20)
 price = models.CharField(max_length=20)

 def __unicode__(self):
  return self.youtube

