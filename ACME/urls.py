from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', include('modules.home.urls')),
    path('clientes', include('modules.clientes.urls')),
    path('accounts/', include('users.urls')),
]
