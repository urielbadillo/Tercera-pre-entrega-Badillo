from django.template import Template, Context, loader
from django.http import HttpResponse


def casita (request):
    return HttpResponse("Bienvenidos al sitio de aqui")
