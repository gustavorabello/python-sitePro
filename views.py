# Create your views here.

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

def index(request):
 return render_to_response('about.html',
                           context_instance=RequestContext(request,settings.CONTEXT))

