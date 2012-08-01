# Create your views here.

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from sales.models import Sale

def index(request):
 m = Sale.objects.all()

 return render_to_response('sales.html',
                           {
                            'sale_list':m,
                           },
                           context_instance=
                           RequestContext(request,settings.CONTEXT))
