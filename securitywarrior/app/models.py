from django.db import models

# Create your models here.
# Appliance, cursos, servicios, eventos


class Appliance(models.Model):
    compania = models.CharField(max_length=40)
    costo = models.IntegerField()
    licencia = models.CharField(max_length=40)


class Cursos(models.Model):
    nombre = models.CharField(max_length=40)
    costo = models.IntegerField()
    tiempo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)


class Servicios(models.Model):
    nombre = models.CharField(max_length=40)
    costo = models.IntegerField()
    caracteristicas = models.CharField(max_length=40)


class Eventos(models.Model):
    nombre = models.CharField(max_length=40)
    fecha = models.DateField()
    costo = models.IntegerField()
    lugar = models.CharField(max_length=40)
