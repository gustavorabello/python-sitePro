# Create your views here.

from django.conf import settings
from polls.models import Poll
from django.template import loader,Context,RequestContext
from django.http import HttpResponse

def index(request):
 #c = Context(settings.CONTEXT)
 c = RequestContext(request)
 t = loader.get_template('about.html')
 return HttpResponse(t.render(c))

def detail(request, poll_id):
     return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
 return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
 return HttpResponse("You're voting on poll %s." % poll_id)
