# Create your views here.

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from videos.models import Video

def index(request):
 m = Video.objects.all()

 return render_to_response('videos.html',
                           {
                            'video_list':m,
                           },
                           context_instance=
                           RequestContext(request,settings.CONTEXT))
