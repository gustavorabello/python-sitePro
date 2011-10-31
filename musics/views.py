# Create your views here.

from django.conf import settings
from django.shortcuts import render_to_response,get_object_or_404
from musics.models import Music
from django.template import RequestContext
from django.http import HttpResponse,Http404

def index(request):
 m = Music.objects.all()
 return render_to_response('cifras/index.html',
                           {
                            'music_list':m,
                           },
                           context_instance=
                           RequestContext(request,settings.CONTEXT))


def detail(request,artist_id,song_id):
 return render_to_response('musics/'+artist_id+'/'+song_id,
                           context_instance=
                           RequestContext(request,settings.CONTEXT))

                           
