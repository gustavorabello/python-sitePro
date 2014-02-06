from django.db import models

class Article(models.Model):
 number = models.CharField(max_length=10)
 year = models.CharField(max_length=4)
 title = models.CharField(max_length=500)
 book = models.CharField(max_length=500)
 publisher = models.CharField(max_length=500)
 place = models.CharField(max_length=20)
 name = models.CharField(max_length=20)
 city = models.CharField(max_length=50)
 country = models.CharField(max_length=50)
 kind = models.CharField(max_length=50)
 addinfo = models.CharField(max_length=10000)
 doi = models.CharField(max_length=50)

 def __unicode__(self):
  return self.abstract

