import django.contrib.admin.templatetags.admin_modify
from . import views,api
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import auth_login


urlpatterns = [
    path('', views.home, name='home'),
    path('data/', views.dht11, name='Data'),
    path('api/list', api.Dlist, name='DHT11List'),
    # genericViews
    path('api/post', api.Dhtviews.as_view(), name='DHT_post'),
    path('csv/', views.exp_csv, name='exp-csv'),
    path('pdf', views.pdf, name='pdf'),
    ##api
    ]
