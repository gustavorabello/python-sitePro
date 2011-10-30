# Create your views here.

from django.conf import settings
from django.shortcuts import render_to_response,get_object_or_404
from musics.models import Music
from django.template import RequestContext
from django.http import HttpResponse,Http404

def index(request):
 return render_to_response('cifras/index.html',
                           context_instance=RequestContext(request,settings.CONTEXT))

def detail(request, music_id):
 #m = get_object_or_404(Music, pk=music_id)
 m = Music.objects.all()
 return render_to_response('cifras/regraTres.html',{'music_list':m})

                           
