from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect,HttpResponseForbidden
from django.urls import reverse
from django.contrib import  messages
from django.contrib.auth import *
from django.contrib.auth.forms import *
from django.template import loader
from .models import *
from .forms import *

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def cities(request):
    template = loader.get_template('cities.html')
    context = {
        'cities' : City.objects.all(),
        'title': 'Список Городов',
        'power_user': request.user.groups.filter(name='admin').exists(),
    }
    return HttpResponse(template.render(context, request))

def streets(request):
    template = loader.get_template('streets.html')
    context = {
        'streets' : Street.objects.all(),
        'title': 'Список улиц',
        'power_user': request.user.groups.filter(name='admin').exists()
    }
    return HttpResponse(template.render(context, request))

def pharmacy(request):
    template = loader.get_template('pharmacy.html')
    context = {
        'pharmacies' : Pharmacy.objects.all(),
        'title': 'Список аптек',
        'power_user': request.user.groups.filter(name='admin').exists()
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

def place(request):
    template = loader.get_template('place.html')
    context = {
        'place' : Place.objects.all(),
        'title': 'Список количества лекарства',
        'power_user': request.user.groups.filter(name='admin').exists()
    }
    return HttpResponse(template.render(context, request))

def new_pharmacy(request):
    if request.user.is_authenticated:
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
            'title':'Добавление аптеки'
        }
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponseForbidden("<h1>Доступ запрещён</h1>")

def new_cures(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CuresForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('cure'))
        else:
            form = CuresForm()
        template = loader.get_template('cures.form.html')
        context = {
            'form': form,
            'title':'Добавление лекарства'
        }
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponseForbidden("<h1>Доступ запрещён</h1>")

def new_street(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = StreetForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('streets'))
        else:
            form = StreetForm()
        template = loader.get_template('street_form.html')
        context = {
            'form': form,
            'title':'Добавление улицы'
        }
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponseForbidden("<h1>Доступ запрещён</h1>")


def new_cities(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CityForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('cities'))
        else:
            form = CityForm()
        template = loader.get_template('city_form.html')
        context = {
            'form': form,
            'title':'Добавление города'
        }
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponseForbidden("<h1>Доступ запрещён</h1>")

def new_place(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PlaceForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('place'))
        else:
            form = PlaceForm()
        template = loader.get_template('place_form.html')
        context = {
            'form': form,
            'title':'Добавление'
        }
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponseForbidden("<h1>Доступ запрещён</h1>")

def edit_cures(request,kp):
    if request.user.is_authenticated:
        try:
            cure = Cure.objects.get(id=kp)
        except Cure.DoesNotExist:
            raise Http404("Лекарство с кодом " + str(kp) + " не найдена")

        if request.method == 'POST':
            form = CuresForm(request.POST, instance=cure)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('cure'))
        else:
            form = CuresForm(instance=cure)

        template = loader.get_template('cures.form.html')
        context = {
            'form':form,
            'title':'Редактирование лекарства'
        }
        return  HttpResponse(template.render(context,request))
    else:
        return HttpResponseForbidden("<h1>Доступ запрещён</h1>")

def edit_pharmacy(request,kp):
    if request.user.is_authenticated:
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
    else:
        return HttpResponseForbidden("<h1>Доступ запрещён</h1>")

def edit_place(request,kp):
    if request.user.is_authenticated:
        try:
            place = Place.objects.get(id=kp)
        except Place.DoesNotExist:
            raise Http404("Аптека с кодом " + str(kp) + " не найдена")

        if request.method == 'POST':
            form = PlaceForm(request.POST, instance=place)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('place'))
        else:
            form = PlaceForm(instance=place)

        template = loader.get_template('place_form.html')
        context = {
            'form':form,
            'title':'Редактирование аптеки'
        }
        return  HttpResponse(template.render(context,request))
    else:
        return HttpResponseForbidden("<h1>Доступ запрещён</h1>")

def edit_street(request,kp):
    if request.user.is_authenticated:
        try:
            street = Street.objects.get(id=kp)
        except Street.DoesNotExist:
            raise Http404("Улица с кодом " + str(kp) + " не найдена")

        if request.method == 'POST':
            form = StreetForm(request.POST, instance=street)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('streets'))
        else:
            form = StreetForm(instance=street)

        template = loader.get_template('street_form.html')
        context = {
            'form':form,
            'title':'Редактирование улицы'
        }
        return  HttpResponse(template.render(context,request))
    else:
        return HttpResponseForbidden("<h1>Доступ запрещён</h1>")

def edit_cities(request,kp):
    if request.user.is_authenticated:
        try:
            city = City.objects.get(id=kp)
        except City.DoesNotExist:
            raise Http404("Город с кодом " + str(kp) + " не найдена")

        if request.method == 'POST':
            form = CityForm(request.POST, instance=city)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('cities'))
        else:
            form = CityForm(instance=city)

        template = loader.get_template('city_form.html')
        context = {
            'form':form,
            'title':'Редактирование города'
        }
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponseForbidden("<h1>Доступ запрещён</h1>")

def del_cities(request, kp):
    if request.user.is_authenticated:
        try:
            city = City.objects.get(id=kp)
        except City.DoesNotExist:
            raise Http404("Город с кодом " + str(kp) + " не найден")
        m = f"Город {city.name} удалён"
        city.delete()
        messages.error(request,m)
        return HttpResponseRedirect(reverse('cities'))
    else:
        return HttpResponseForbidden("<h1>Доступ запрещён</h1>")

def del_place(request, kp):
    if request.user.is_authenticated:
        try:
            place = Place.objects.get(id=kp)
        except Place.DoesNotExist:
            raise Http404("Город с кодом " + str(kp) + " не найден")
        m = f"Город {place} удалён"
        place.delete()
        messages.error(request,m)
        return HttpResponseRedirect(reverse('place'))
    else:
        return HttpResponseForbidden("<h1>Доступ запрещён</h1>")

def del_cures(request, kp):
    if request.user.is_authenticated:
        try:
            cure = Cure.objects.get(id=kp)
        except Cure.DoesNotExist:
            raise Http404("Лекарство с кодом " + str(kp) + " не найдено")
        m = f"Лекарство {cure.name} удалёно"
        cure.delete()
        messages.error(request,m)
        return HttpResponseRedirect(reverse('cures'))
    else:
        return HttpResponseForbidden("<h1>Доступ запрещён</h1>")

def del_street(request, kp):
    if request.user.is_authenticated:
        try:
            street = Street.objects.get(id=kp)
        except Street.DoesNotExist:
            raise Http404("Улица с кодом " + str(kp) + " не найдена")
        m = f"Улица {street.name} удалёна"
        street.delete()
        messages.error(request,m)
        return HttpResponseRedirect(reverse('streets'))
    else:
        return HttpResponseForbidden("<h1>Доступ запрещён</h1>")

def del_pharmacy(request, kp):
    if request.user.is_authenticated:
        try:
            pharmacy = Pharmacy.objects.get(id=kp)
        except Pharmacy.DoesNotExist:
            raise Http404("Аптека с кодом " + str(kp) + " не найдена")
        m = f"Аптека {pharmacy.name} удалена"
        pharmacy.delete()
        messages.error(request,m)
        return HttpResponseRedirect(reverse('pharmacies'))
    else:
        return HttpResponseForbidden("<h1>Доступ запрещён</h1>")

def cures(request):
    template = loader.get_template('cures.html')
    context = {
        'cures' : Cure.objects.all(),
        'title': 'Список лекарств'
    }
    return HttpResponse(template.render(context, request))

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()
    template = loader.get_template('user_form.html')
    context = {
        'form': form,
        'title':'Создание пользоавтеля'
    }
    return HttpResponse(template.render(context,request))

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username=username,password=userpass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = AuthenticationForm()
    template = loader.get_template('user_form.html')
    context = {
        'form': form,
        'title':'Вход в систему'
    }
    return HttpResponse(template.render(context,request))


def logout_user(request):
    logout(request)
    messages.success(request, 'Вы вышли из системы')
    return HttpResponseRedirect(reverse('index'))