from django.urls import path, include
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("appliance/", appliance_vista, name="appliance"),
    path("cursos/", cursos_vista, name="cursos"),
    path("eventos/", eventos_vista, name="eventos"),
    path("servicios/", servicios_vista, name="servicios"),
    path("formularios/", formularios_vista, name="formularios"),
    path("appliance_form/", appliance_form, name="appliance_form"),
    path("curso_form/", cursos_form, name="curso_form"),
    path("servicios_form/", servicios_form, name="servicios_form"),
    path("eventos_form/", eventos_form, name="eventos_form"),
]
