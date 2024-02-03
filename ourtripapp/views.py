from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import DayProgram
from .models import Tripper
from .models import Badge
from .models import Title

def index(request):
    title = Title.objects.order_by('id').last()

    tripdaylist = DayProgram.objects.order_by('tripdate') & DayProgram.objects.filter(part_of_trip_id=title.id)
    tripperlist = Tripper.objects.order_by('tripper')
    #title = Title.objects.filter(id=tripdaylist[0].part_of_trip_id)
    template = loader.get_template('ourtripapp/index.html')
    context = {
        'tripdaylist': tripdaylist,
        'tripperlist': tripperlist,
        'title' : title,
    }
    return HttpResponse(template.render(context, request))

def trips(request):
    triplist = Title.objects.order_by('id')
    template = loader.get_template('ourtripapp/trips.html')
    context = {
        'triplist': triplist,
    }
    return HttpResponse(template.render(context, request))

def tripindex(request,id):
    title = Title.objects.filter(pk=id)
    tripdaylist = DayProgram.objects.filter(part_of_trip_id=title[0].id)
    tripperlist = Tripper.objects.order_by('tripper')
    template = loader.get_template('ourtripapp/tripindex.html')
    context = {
        'tripdaylist': tripdaylist,
        'tripperlist': tripperlist,
        'title' : title,
    }
    return HttpResponse(template.render(context, request))


def detail(request,id):
    tripday = DayProgram.objects.filter(id=id)
    template = loader.get_template('ourtripapp/detail.html')
    context = {
        'tripday': tripday,
    }
    return HttpResponse(template.render(context, request))

def tripper(request,tripper):
    tripper=Badge.objects.filter(tripper__tripper=tripper)
    trippername = tripper
    template = loader.get_template('ourtripapp/tripper.html')
    context = {
        'tripper' : tripper,
        'trippername' : trippername,
    }
    return HttpResponse(template.render(context, request))


