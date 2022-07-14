from django.db import models

# Create your models here.
# 
class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    Precio = models.IntegerField
    disponible = models.BooleanField()
    foto = models.CharField(max_length=30)

    

  #ESTO EQUIVALE A CREAR UNA TABLA CON ESTOS CAMPOS SIN NECESIDAD DE SABER SQL
