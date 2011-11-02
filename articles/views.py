# Create your views here.

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from articles.models import Article 

def index(request):
 return render_to_response('articles.html',
                           context_instance=RequestContext(request,settings.CONTEXT))

def index2(request):
 m = Article.objects.all()

 return render_to_response('articles2.html',
                           {
                            'article_list':m,
                           },
                           context_instance=
                           RequestContext(request,settings.CONTEXT))
