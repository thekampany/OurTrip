from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import DayProgram
from .models import Tripper
from .models import Badge
from .models import Title

def index(request):
    tripdaylist = DayProgram.objects.order_by('tripdate')
    tripperlist = Tripper.objects.order_by('tripper')
    title = Title.objects.order_by('title')
    template = loader.get_template('ourtripapp/index.html')
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


