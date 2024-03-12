from django.shortcuts import render
from .models import *

# Create your views here.
def home (request):
    return  render(request, "app/index.html")


def appliance_vista (request):
    contexto = {'appliance': appliance.objects.all()}
    return  render(request, "app/appliance.html", contexto)

def cursos_vista (request):
    return  render(request, "app/cursos.html")

def servicios_vista (request):
    return  render(request, "app/servicios.html")

def eventos_vista (request):
    return  render(request, "app/eventos.html")