## =================================================================== ##
#  this is file setup.py, created at 30-Oct-2011                #
#  maintained by Gustavo Rabello dos Anjos                              #
#  e-mail: gustavo.rabello@gmail.com                                    #
## =================================================================== ##

import os,fnmatch,re,shutil,socket
from django.conf import settings
from PIL import Image

os.environ['DJANGO_SETTINGS_MODULE'] = u"settings"

def populateArticleDB():
 from articles.models import Article

 dirname = 'static/articles/'

 print ""
 print " ************************************* "
 print " *  Adding entries to the database:  * "
 print ""

 # loop all files
 for arq in os.listdir(dirname):

  if fnmatch.fnmatch(arq, '*.txt'): 
   # spliting base name and extension
   basename = os.path.splitext(arq)[0]
   filename = basename + '.pdf'
     
   fopen = open(dirname+arq,'r')
   line = fopen.readlines()

   title = line[0].split('\n')[0]
   year  = line[2].split('\n')[0]
   month = line[4].split('\n')[0]
   place = line[6].split('\n')[0]
   kind  = line[8].split('\n')[0]
   abstract = line[10].split('\n')[0]
   
   # saving in the database
   art = Article(filename=filename,
                 year=year,
                 month=month,
                 title=title,
                 place=place,
                 kind=kind,
                 abstract=abstract)
  
   print "   " + filename + ' added'
   art.save()

 print ""
 print " *  Entries in the database ADDED:   * "
 print " ************************************* "
 print ""

def populateVideoDB():
 from videos.models import Video
 import gdata.youtube
 import gdata.youtube.service

 print ""
 print " ************************************* "
 print " *  Adding entries to the database:  * "
 print ""

 yt_service = gdata.youtube.service.YouTubeService()
 pl_id = 'A5C4DB7CAE7AF003'
 playlist_video_feed = yt_service.GetYouTubePlaylistVideoFeed(playlist_id=pl_id)
 for entry in playlist_video_feed.entry:
  title =  entry.media.title.text
  youtube = 'http://www.youtube.com/embed/%s' % entry.media.player.url[32:43]
  description = entry.media.description.text
  duration = entry.media.duration.seconds

  # saving in the database
  v = Video(title=title,
            youtube=youtube,
            description=description,
            time=duration)
  
  print "   " + title + ' added'
  v.save()
    
 print ""
 print " *  Entries in the database ADDED:   * "
 print " ************************************* "
 print ""

def populateMusicDB():
 from musics.models import Music

 dirname = 'static/cifras/'

 print ""
 print " ************************************* "
 print " *  Adding entries to the database:  * "
 print ""

 # loop all artist's folder
 for artistname in os.listdir(dirname):
  # loop inside each folder
  if os.path.isdir(os.path.join(dirname, artistname)):
   for infile in os.listdir(dirname+artistname):
    if fnmatch.fnmatch(infile, '*.html'): 
     # spliting base name and extension
     basename = os.path.splitext(infile)[0]
     
     # HTML files should be formatted as follow:
     # oCarderno.html,
     # maisQueNada.html,
     # escravoDaAlegria.html etc.
     #
     # spliting basename in several words, ex:
     # myNameIsGustavo ---> my Name Is Gustavo
     splitsongname = re.sub(r'(?<=.)([A-Z])', r' \1', basename).split()

     songname=''
     for name in splitsongname: 
     # function: my Name Is Gustavo --> My Name Is Gustavo
      songname += name.title() + " "
 
     splitartistname = re.sub(r'(?<=.)([A-Z])', r' \1', artistname).split()
 
     artist=''
     for name in splitartistname: 
      # function: toquinho E Vinicius --> Toquinho E Vinicius
      artist += name.title() + " "
 
     # saving in the database
     m = Music(filename=infile,
               artist=artist,
               artistdir=artistname,
               song=songname,
               year=1967)
    
     print "   " + songname, artist, 1967
     m.save()
 
 print ""
 print " *  Entries in the database ADDED:   * "
 print " ************************************* "
 print ""

def convertImages():

 # retrieving default context dictionary from settings
 if socket.gethostname() == 'alkalurops':
  deploy_dir = os.getenv("HOME") + '/misc.rabello.org/'
 else:
  deploy_dir = os.path.dirname(__file__) + 'deploy'
 
 deploy_static_dir = os.path.join(deploy_dir,'static')
 
 print u"Removing existing deploy dir, if any..."
 shutil.rmtree(deploy_dir,ignore_errors=True)
 
 print u"Creating deploy/ dir..."
 os.mkdir(deploy_dir)

 print u"Copying contents of static/ into deploy/static/css..."
 deploy_css_dir = os.path.join(deploy_static_dir,'css')
 shutil.copytree(settings.CSS_DIR,deploy_css_dir)

 print u"Copying contents of pdf into deploy/static/pdf..."
 deploy_pdf_dir = os.path.join(deploy_static_dir,'pdf')
 shutil.copytree(settings.PDF_DIR,deploy_pdf_dir)

 print u"Copying contents of ppts(pdfs) into deploy/static/ppt..."
 deploy_ppt_dir = os.path.join(deploy_static_dir,'ppt')
 shutil.copytree(settings.PPT_DIR,deploy_ppt_dir)

 print u"Copying contents of html into deploy/static/html..."
 deploy_html_dir = os.path.join(deploy_static_dir,'html')
 shutil.copytree(settings.HTML_DIR,deploy_html_dir)

 print u"Copying contents of cifras into deploy/static/cifras..."
 deploy_cifras_dir = os.path.join(deploy_static_dir,'cifras')
 shutil.copytree(settings.CIFRAS_DIR,deploy_cifras_dir)

 print u"Creating images and thumbnails directories..."
 deploy_thumb16_path  = os.path.join(deploy_static_dir,'thumbs16')
 deploy_thumb32_path  = os.path.join(deploy_static_dir,'thumbs32')
 deploy_thumb64_path  = os.path.join(deploy_static_dir,'thumbs64')
 deploy_thumb128_path = os.path.join(deploy_static_dir,'thumbs128')
 deploy_image_path = os.path.join(deploy_static_dir,'images')
 os.mkdir(deploy_thumb16_path)
 os.mkdir(deploy_thumb32_path)
 os.mkdir(deploy_thumb64_path)
 os.mkdir(deploy_thumb128_path)
 os.mkdir(deploy_image_path)

 images = []
 images_dict = {}
 images_dir = settings.IMAGE_DIR
 thumb_format = settings.STATIC_THUMBNAIL_FORMAT
 image_format = settings.STATIC_IMAGE_FORMAT
 thumb_dim16  = settings.THUMBNAIL_SIZE16
 thumb_dim32  = settings.THUMBNAIL_SIZE32
 thumb_dim64  = settings.THUMBNAIL_SIZE64
 thumb_dim128 = settings.THUMBNAIL_SIZE128
 for filename in os.listdir(images_dir):
  # only process if ends with image file extension
  before_ext,ext = os.path.splitext(filename)
  if ext not in (".png",".jpg",):
      continue

  print u"Copying image and thumbnailing %s..." % filename
  filepath = os.path.join(images_dir,filename)
  im = Image.open(filepath)

  # save images
  im.save(os.path.join(deploy_image_path, filename),"PNG")

  # save thumbnails 16x16, 32x32, 64x64 and 128x128
  im.thumbnail(thumb_dim128, Image.ANTIALIAS)
  im.save(os.path.join(deploy_thumb128_path, filename), "PNG")
  im.thumbnail(thumb_dim64, Image.ANTIALIAS)
  im.save(os.path.join(deploy_thumb64_path, filename), "PNG")
  im.thumbnail(thumb_dim32, Image.ANTIALIAS)
  im.save(os.path.join(deploy_thumb32_path, filename), "PNG")
  im.thumbnail(thumb_dim16, Image.ANTIALIAS)
  im.save(os.path.join(deploy_thumb16_path, filename), "PNG")

def deleteDB():
 os.remove( os.path.join(os.path.dirname(__file__),'../database') )

def createDB():
 os.system('python manage.py syncdb')

def main():
 deleteDB()
 createDB()
 convertImages()
 populateMusicDB()
 populateVideoDB()
 populateArticleDB()

 # completed build script
 print u"All done running build.py."


if __name__ == "__main__":
    main()


