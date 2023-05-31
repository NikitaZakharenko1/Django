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