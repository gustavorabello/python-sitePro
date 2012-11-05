# Create your views here.

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from images.models import Image

def index(request):
 m = Image.objects.all()

 return render_to_response('images.html',
                           {
                            'image_list':m,
                           },
                           context_instance=
                           RequestContext(request,settings.CONTEXT))
