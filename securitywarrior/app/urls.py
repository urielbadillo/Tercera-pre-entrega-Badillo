from django.urls import path, include
from .views import * 


urlpatterns = [
    path('', home, name="home"),
    path('appliance/', appliance, name="appliance"),
    path('cursos/', cursos, name="cursos"),
    path('eventos/', eventos, name="eventos"),
    path('servicios/', servicios, name="servicios"),

]
