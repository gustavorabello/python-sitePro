## =================================================================== ##
#  this is file setup.py, created at 30-Oct-2011                #
#  maintained by Gustavo Rabello dos Anjos                              #
#  e-mail: gustavo.rabello@gmail.com                                    #
## =================================================================== ##

import os 
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = u"settings"

from musics.models import Music

m = Music(artist='toquinho',song='regra tres',year=1967)
m.save()
m = Music(artist='toquinho',song='testamento',year=1968)
m.save()
m = Music(artist='baden powell',song='berimbau',year=1962)
m.save()



