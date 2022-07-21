from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import auth_login

urlpatterns = [
    path('inscription', views.inscriptionpage,name='inscription'),
    path('acces', views.accespage,name='acces'),
    path('quitter', views.logoutUser,name='quitter'),

]