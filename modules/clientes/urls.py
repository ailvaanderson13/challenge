from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.ListClients.as_view(), name='clientes'),
    path('add-filial/',
         views.AddFilial.as_view(), name='add-filial'),
]
