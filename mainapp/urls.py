from django.urls import path

from . import views

urlpatterns = [
    path("pharmacies/", views.pharmacy,name='pharmacies'),
    path("", views.index, name="index"),
]
