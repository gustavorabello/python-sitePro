# Create your views here.

from django.conf import settings
from django.template import loader,Context
from django.http import HttpResponse,Http404

def index(request):
 raise Http404
#--------------------------------------------------
#  c = Context(settings.CONTEXT)
#  t = loader.get_template('index.html')
#  return HttpResponse(t.render(c))
#-------------------------------------------------- 

