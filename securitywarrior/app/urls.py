from django.urls import path, include
from .views import * 


urlpatterns = [
    path('', home, name="home"),
    path('appliance/', appliance_vista, name="appliance"),
    path('cursos/', cursos_vista, name="cursos"),
    path('eventos/', eventos_vista, name="eventos"),
    path('servicios/', servicios_vista, name="servicios"),

]
