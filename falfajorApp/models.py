from django.db import models

# Create your models here.
class Alfajor(models.Model):

    nombre=models.CharField(max_length=40)
    codigo_alfajor = models.IntegerField()


class Clientes(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    telefono= models.IntegerField()


class Pedidos(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()