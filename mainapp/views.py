from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader
from .models import *

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def pharmacy(request):
    template = loader.get_template('pharmacy.html')
    context = {
        'pharmacies' : Pharmacy.objects.all(),
        'title': 'Список аптек'
    }
    return HttpResponse(template.render(context, request))

def cures(request):
    template = loader.get_template('cures.html')
    context = {
        'cures' : Cure.objects.all(),
        'title': 'Список лекарств'
    }
    return HttpResponse(template.render(context, request))

def cure(request,dk):
    try:
        cure = Cure.objects.get(id=dk)
    except Cure.DoesNotExist:
        raise Http404("Лекарство с кодом " + str(dk) + " не найдено!")

    template = loader.get_template('cure.html')
    context = {
        'cure' : cure,
        'title': cure.name
    }
    return HttpResponse(template.render(context, request))


