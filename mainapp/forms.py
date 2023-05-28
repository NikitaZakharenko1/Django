from django.forms import ModelForm
from . import models


class PharmacyForm(ModelForm):
    class Meta:
        model = models.Pharmacy
        fields = ['name','street']