from django.http import HttpResponse
import datetime
from django.shortcuts import render,redirect
from django.template import Template, Context
from productos.models import Productos
import random

def saludo(request):
  
  doc_externo=open("static\index.html")
  plt=Template(doc_externo.read())
  doc_externo.close()
  ctx = Context()
  documento=plt.render(ctx)
  return HttpResponse(documento)

def tienda(request):
      
  doc_externo=open("static\tienda.html")
  plt=Template(doc_externo.read())
  doc_externo.close()
  ctx = Context()
  documento=plt.render(ctx)
  return HttpResponse(documento)


def tienda(request):
  return render(request,"tienda.html")


def about(request):
      
  doc_externo=open("static\QuienesSomos.html")
  plt=Template(doc_externo.read())
  doc_externo.close()
  ctx = Context()
  documento=plt.render(ctx)
  return HttpResponse(documento)


def login(request):
      
  doc_externo=open("static\loginyregistro.html")
  plt=Template(doc_externo.read())
  doc_externo.close()
  ctx = Context()
  documento=plt.render(ctx)
  return HttpResponse(documento)



def seguimiento(request):
      
  doc_externo=open("static\seguimiento.html")
  plt=Template(doc_externo.read())
  doc_externo.close()
  ctx = Context()
  documento=plt.render(ctx)
  return HttpResponse(documento)

def productobd(request):
  productos = Productos.objects.all()
  contexto = {'listadoproductos':productos}
  return render (request,'tienda.html',contexto)


def CRUD(request):
      
  doc_externo=open("static\crud.html")
  plt=Template(doc_externo.read())
  doc_externo.close()
  ctx = Context()
  documento=plt.render(ctx)
  return HttpResponse(documento)


def eliminarproducto(request,id):
  productoborrar = Productos.objects.get(id=id)
  productoborrar.delete()
  return redirect('/crud.html/')

def agregarproducto(request,id):

  Productos.objects.create(
                            nombre="jabon",
                            disponible="true",
                            foto="{%static 'img\07fd23c4-e8ed-400c-bde4-61e7daa40252.jpg'%}")
  return redirect('/crud.html/')




  