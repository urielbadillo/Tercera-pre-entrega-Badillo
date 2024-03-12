from django.db import models

# Create your models here.
# Appliance, cursos, servicios, eventos


class appliance(models.Model):
    compañia = models.CharField(max_length=40)
    costo = models.IntegerField()
    licencia = models.CharField(max_length=40)


class cursos(models.Model):
    nombre = models.CharField(max_length=40)
    costo = models.IntegerField()
    tiempo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)


class servicios(models.Model):
    nombre = models.CharField(max_length=40)
    costo = models.IntegerField()
    caracteristicas = models.CharField(max_length=40)


class eventos(models.Model):
    nombre = models.CharField(max_length=40)
    fecha = models.DateField()
    costo = models.IntegerField()
    lugar = models.CharField(max_length=40)
