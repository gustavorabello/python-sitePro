from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('musics.views',
  # Examples:
  (r'^$', 'index'),
  (r'^(?P<music_id>\d+)/$', 'detail'),

  #url(r'^admin/', include(admin.site.urls)),
)

