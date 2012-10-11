# Create your views here.

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from recipes.models import Recipe

def index(request):
 m = Recipe.objects.all()

 return render_to_response('recipes.html',
                           {
                            'recipe_list':m,
                           },
                           context_instance=
                           RequestContext(request,settings.CONTEXT))
