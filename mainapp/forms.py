from django.forms import ModelForm
from . import models


class PharmacyForm(ModelForm):
    class Meta:
        model = models.Pharmacy
        fields = ['name','street']

class CityForm(ModelForm):
    class Meta:
        model = models.City
        fields = ['name']

class StreetForm(ModelForm):
    class Meta:
        model = models.Street
        fields = ['name','city']

class PlaceForm(ModelForm):
    class Meta:
        model = models.Place
        fields = ['cure','quantity']