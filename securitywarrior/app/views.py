from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "app/index.html")


def appliance_vista(request):
    contexto = {"appliance": Appliance.objects.all()}
    return render(request, "app/appliance.html", contexto)


def cursos_vista(request):
    contexto = {"cursitoss": Cursos.objects.all()}
    return render(request, "app/cursos.html", contexto)


def servicios_vista(request):
    contexto = {"servicitoo": Servicios.objects.all()}
    return render(request, "app/servicios.html", contexto)


def eventos_vista(request):
    contexto = {"eventitos": Eventos.objects.all()}
    return render(request, "app/eventos.html", contexto)


def formularios_vista(request):
    return render(request, "app/formularios_index.html")


# Formularios


def appliance_form(request):
    if request.method == "POST":
        miform = Appliance_Forms(request.POST)
        if miform.is_valid():
            appliance_compania = miform.cleaned_data.get("compania")
            appliance_costo = miform.cleaned_data.get("costo")
            appliance_licencia = miform.cleaned_data.get("licencia")
            appliances = Appliance(
                compania=appliance_compania,
                costo=appliance_costo,
                licencia=appliance_licencia,
            )
            appliances.save()
            return render(request, "app/index.html")
    else:
        miform = Appliance_Forms()
    return render(request, "app/appliance_form.html", {"form": miform})


def cursos_form(request):
    if request.method == "POST":
        miform = Cursos_Forms(request.POST)
        if miform.is_valid():
            curso_nombre = miform.cleaned_data.get("nombre")
            curso_costo = miform.cleaned_data.get("costo")
            curso_tiempo = miform.cleaned_data.get("tiempo")
            curso_descripcion = miform.cleaned_data.get("descripcion")
            cursitos = Cursos(
                nombre=curso_nombre,
                costo=curso_costo,
                tiempo=curso_tiempo,
                descripcion=curso_descripcion,
            )
            cursitos.save()
            return render(request, "app/index.html")
    else:
        miform = Cursos_Forms()
    return render(request, "app/curso_form.html", {"form": miform})


def servicios_form(request):
    if request.method == "POST":
        miform = Servicios_Forms(request.POST)
        if miform.is_valid():
            servicio_nombre = miform.cleaned_data.get("nombre")
            servicio_costo = miform.cleaned_data.get("costo")
            servicio_caracteristicas = miform.cleaned_data.get("caracteristicas")
            servicito = Servicios(
                nombre=servicio_nombre,
                costo=servicio_costo,
                caracteristicas=servicio_caracteristicas,
            )
            servicito.save()
            return render(request, "app/index.html")
    else:
        miform = Servicios_Forms()
    return render(request, "app/servicios_form.html", {"form": miform})


def eventos_form(request):
    if request.method == "POST":
        miform = Eventos_Forms(request.POST)
        if miform.is_valid():
            evento_nombre = miform.cleaned_data.get("nombre")
            evento_fecha = miform.cleaned_data.get("fecha")
            evento_costo = miform.cleaned_data.get("costo")
            evento_lugar = miform.cleaned_data.get("lugar")
            eventito = Eventos(
                nombre=evento_nombre,
                fecha=evento_fecha,
                costo=evento_costo,
                lugar=evento_lugar,
            )
            eventito.save()
            return render(request, "app/index.html")
    else:
        miform = Eventos_Forms()
    return render(request, "app/eventos_form.html", {"form": miform})
