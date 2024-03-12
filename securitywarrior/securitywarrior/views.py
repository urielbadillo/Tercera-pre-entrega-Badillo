from django.template import Template, Context, loader
from django.http import HttpResponse
import datetime
from app.models import * 

def nuevo_appliance(request):
    icompañia = "Fortinet"
    icosto = int(25000)
    ilicencia = "Propietario"
    napllieance = appliance (compañia=icompañia, costo=icosto, licencia=ilicencia)
    appliance.save()
    respuesta = f"<html><h1>Appliance gurdado</h1></html>"
    return HttpResponse(respuesta)