from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request):
  
  doc_externo=open("static\index.html")
  plt=Template(doc_externo.read())
  doc_externo.close()
  ctx = Context()
  documento=plt.render(ctx)
  return HttpResponse(documento)

def quienesSomos(request):
      
  doc_externo=open("static\QuienesSomos.html")
  plt=Template(doc_externo.read())
  doc_externo.close()
  ctx = Context()
  documento=plt.render(ctx)
  return HttpResponse(documento)


