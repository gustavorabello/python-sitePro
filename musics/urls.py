from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('musics.views',
  # Examples:
  (r'^$', 'index'),
  #(r'^(?P<music_id>\d+)/$', 'detail'),

  (r'^(?P<artist_id>\W+)/(?P<song_id>\W+)/$', 'detail'),
  #(r'^(?P<artist_id>\w+)/$', 'detail'),
  #(r'^(?P<artist_id>\d+)/baden/$', 'detail'),
  #(r'^baden/$', 'detail'),

  #url(r'^admin/', include(admin.site.urls)),
)

