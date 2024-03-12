from django.shortcuts import render

# Create your views here.
def home (request):
    return  render(request, "app/index.html")


def appliance (request):
    return  render(request, "app/appliance.html")

def cursos (request):
    return  render(request, "app/cursos.html")

def servicios (request):
    return  render(request, "app/servicios.html")

def eventos (request):
    return  render(request, "app/eventos.html")