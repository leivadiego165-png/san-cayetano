from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)

class Factura(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    consumo = models.IntegerField()
    total = models.IntegerField()
