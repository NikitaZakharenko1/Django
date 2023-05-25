from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
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


