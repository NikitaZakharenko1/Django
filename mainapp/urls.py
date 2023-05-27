from django.urls import path

from . import views

urlpatterns = [
    path("pharmacies/", views.pharmacy,name='pharmacies'),
    path("cures/", views.cures,name='cures'),
    path("cure/<int:dk>",views.cure,name='cure'),
    path("", views.index, name="index"),
]
