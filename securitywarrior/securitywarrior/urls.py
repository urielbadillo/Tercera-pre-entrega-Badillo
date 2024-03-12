from django.contrib import admin
from django.urls import path, include
from securitywarrior.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app.urls")),

]
