# Create your views here.

from stages.models import *
from routes.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson

def all_routes(request, city):
    stages = Stage.objects.filter(city=city)
    data = dict([ (s.id, 
        {'display_name': s.display_name,
         'latitude': s.location.y,
         'longitude': s.locaton.x}
        ) for s in stages])
    return HttpResponse(simplejson.dumps(data))

def single_route(request, city, route_name):
    r = Route.objects.filter(city=city).get(display_name__iexact=route_name)
    return HttpResponse(simplejson.dumps(
            {
            'name': r.display_name,
            'stages': [ { 'name': s.display_name,
                          'latitude': s.location.y,
                          'longitude': s.location.x                          
                        }
                        for s in r.stages.all()]
                        }))

def autocomplete_stages(request, city):
    stages = Stage.objects.filter(city=city)
    data = dict( [ (s.display_name, s.id) for s in stages] )
    return HttpResponse(simplejson.dumps(data))
