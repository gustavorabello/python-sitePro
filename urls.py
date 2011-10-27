from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', include('about.urls')),
    (r'^about/', include('about.urls')),
    (r'^research/', include('research.urls')),
    (r'^articles/', include('articles.urls')),
    (r'^misc/', include('misc.urls')),
    #(r'^images/', include('images.urls')),
    #(r'^videos/', include('videos.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
