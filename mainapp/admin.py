from django.contrib import admin

# Register your models here.
from.models import *

admin.site.register(Cure)
admin.site.register(City)
admin.site.register(Street)
admin.site.register(Pharmacy)
admin.site.register(Place)