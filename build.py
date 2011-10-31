## =================================================================== ##
#  this is file setup.py, created at 30-Oct-2011                #
#  maintained by Gustavo Rabello dos Anjos                              #
#  e-mail: gustavo.rabello@gmail.com                                    #
## =================================================================== ##

import os,fnmatch,re
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = u"settings"

from musics.models import Music

dirname = 'static/cifras/'

for artistname in os.listdir(dirname):
 if os.path.isdir(os.path.join(dirname, artistname)):
  for infile in os.listdir(dirname+artistname):
   if fnmatch.fnmatch(infile, '*.html'): 
    basename = os.path.splitext(infile)[0]
    splitsongname = re.sub(r'(?<=.)([A-Z])', r' \1', basename).split()

    songname=''
    for name in splitsongname:
     songname += name.title() + " "

    m = Music(filename=infile,
              artist=artistname,
              song=songname,
              year=1967)
    print infile, artistname, songname, 1967
    m.save()

