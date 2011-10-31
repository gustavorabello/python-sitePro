# Django settings for sitePro project.
import os, datetime,socket

# URL prefix for static files,
# set DEBUG mode
if socket.gethostname() == 'alkalurops':
 STATIC_URL = 'http://misc.rabello.org/static/'
 DEBUG = TEMPLATE_DEBUG = False
else:
 STATIC_URL = '/static/'
 DEBUG = TEMPLATE_DEBUG = True

ROOT_PATH = os.path.dirname(__file__)
DEPLOY_DIR = os.path.join(ROOT_PATH,'deploy')
STATIC_DIR = os.path.join(ROOT_PATH,'static')
CSS_DIR = os.path.join(STATIC_DIR,'css')
IMAGE_DIR = os.path.join(STATIC_DIR,'images')
PDF_DIR = os.path.join(STATIC_DIR,'pdf')
PPT_DIR = os.path.join(STATIC_DIR,'ppt')
HTML_DIR = os.path.join(STATIC_DIR,'html')
CIFRAS_DIR = os.path.join(STATIC_DIR,'cifras')

ADMINS = (
    # ('Gustavo ANJOS', 'gustavo.rabello@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(ROOT_PATH,'../database'),# Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Zurich'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(ROOT_PATH,'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(ROOT_PATH,'deploy/static')

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
#-------------------------------------------------- 
STATICFILES_DIRS = (
  os.path.join(ROOT_PATH,'static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'th0z=#_@q7g866bo#xt^_!-s8a@v8utqxag0xc=7mli__lh%=s'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'sitePro.urls'

# creating default rendering context
# and setting up some helpful values
STATIC_URL_FORMAT = u"/static/%s"
STATIC_THUMBNAIL_FORMAT = STATIC_URL_FORMAT % u"thumbs/%s"
STATIC_IMAGE_FORMAT = STATIC_URL_FORMAT % u"images/%s"
THUMBNAIL_SIZE16  = (16,16)
THUMBNAIL_SIZE32  = (32,32)
THUMBNAIL_SIZE64  = (64,64)
THUMBNAIL_SIZE128 = (128,128)
WEB_WORK = u"http://ltcm.epfl.ch"
WEB_PERSONAL = u"http://gustavo.rabello.org"
EMAIL = u"gustavo.rabello@gmail.com"
PROJECT_NAME = u"gustavo.rabello.org"

CONTEXT = {
    'web_work':WEB_WORK,
    'web_personal':WEB_PERSONAL,
    'email':EMAIL,
    'project_name':PROJECT_NAME,
    'static_root':STATIC_ROOT,
    'now':datetime.datetime.now(),
}

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.core.context_processors.debug',
  'django.core.context_processors.i18n',
  'django.core.context_processors.media',
  'django.core.context_processors.static',
  'django.contrib.auth.context_processors.auth',
  'django.contrib.messages.context_processors.messages',
)

# setting up working directory paths
TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH,'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    # Added apps:
    'about',
    'research',
    'articles',
    'misc',
    'images',
    'videos',
    'musics',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
