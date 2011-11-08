from django.db import models

class Article(models.Model):
 filename = models.CharField(max_length=50)
 year = models.CharField(max_length=4)
 month = models.CharField(max_length=10)
 title = models.CharField(max_length=500)
 place = models.CharField(max_length=20)
 kind = models.CharField(max_length=20)
 abstract = models.CharField(max_length=5000)

 def __unicode__(self):
  return self.abstract

