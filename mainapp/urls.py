from django.urls import path

from . import views

urlpatterns = [
    path("cities/", views.cities,name='cities'),
    path("streets/", views.streets, name='streets'),
    path("pharmacies/", views.pharmacy,name='pharmacies'),
    path("place/", views.place, name='place'),
    path("cities/new/",views.new_cities,name='new_cities'),
    path("cities/<int:kp>/edit/",views.edit_cities,name='edit_cities'),
    path("cities/<int:kp>/delete/",views.del_cities,name='del_cities'),
    path("pharmacy/new/",views.new_pharmacy,name='new_pharmacy'),
    path("pharmacy/<int:kp>/edit/",views.edit_pharmacy,name='edit_pharmacy'),
    path("pharmacy/<int:kp>/delete/",views.del_pharmacy,name='del_pharmacy'),
    path("cures/", views.cures,name='cures'),
    path("cure/<int:dk>",views.cure,name='cure'),
    path("register/", views.register_user,name='register'),
    path("login/", views.login_user, name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("", views.index, name="index"),
]
