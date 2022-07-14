"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.login),
    path('tienda.html/', views.tienda),
    path('QuienesSomos.html/', views.about),
    path('seguimiento.html/', views.seguimiento),
    path('loginyregistro.html/', views.login),
    path('index.html/',views.saludo),
    path('index.html/tienda.html', views.tienda),
    path('index.html/QuienesSomos.html', views.about),
    path('index.html/Seguimiento.html', views.seguimiento),
    path('index.html/crud.html', views.CRUD),
    path('eliminarproducto/<id>',views.eliminarproducto),
    path('agregarproducto/<id>',views.agregarproducto),
]