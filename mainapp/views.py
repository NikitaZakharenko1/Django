from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib import  messages
from django.template import loader
from .models import *
from .forms import *

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

def new_pharmacy(request):
    if request.method == "POST":
        form = PharmacyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pharmacies'))
    else:
        form = PharmacyForm()
    template = loader.get_template('pharmacy_form.html')
    context = {
        'form': form,
        'title':'добавление аптеки'
    }
    return HttpResponse(template.render(context,request))

def edit_pharmacy(request,kp):
    try:
        pharmacy = Pharmacy.objects.get(id=kp)
    except Pharmacy.DoesNotExist:
        raise Http404("Аптека с кодом " + str(kp) + " не найдена")

    if request.method == 'POST':
        form = PharmacyForm(request.POST, instance=pharmacy)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pharmacies'))
    else:
        form = PharmacyForm(instance=pharmacy)

    template = loader.get_template('pharmacy_form.html')
    context = {
        'form':form,
        'title':'редактирование аптеки'
    }
    return  HttpResponse(template.render(context,request))

def del_pharmacy(request, kp):
    try:
        pharmacy = Pharmacy.objects.get(id=kp)
    except Pharmacy.DoesNotExist:
        raise Http404("Аптека с кодом " + str(kp) + " не найдена")
    m = f"Аптека {pharmacy.name} удалена"
    pharmacy.delete()
    messages.error(request,m)
    return HttpResponseRedirect(reverse('pharmacies'))

def cures(request):
    template = loader.get_template('cures.html')
    context = {
        'cures' : Cure.objects.all(),
        'title': 'Список лекарств'
    }
    return HttpResponse(template.render(context, request))