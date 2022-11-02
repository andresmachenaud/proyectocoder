"""proyectocoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from proyectocoder.views import vista_saludo, dia_hoy, ano_nacimiento, vista_plantilla_bonita, vista_listado_alumnos,vista_listado_alumnos_2
from AppCoder.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',vista_saludo), #el string es el nombre de la ruta en el URL
    path("hoy/<nombre>/", dia_hoy),
    path("ano/<edad>", ano_nacimiento),
    path("inicio/", vista_plantilla_bonita),
    path("alumnos/", vista_listado_alumnos),
    path("alumnos2/", vista_listado_alumnos_2),
    path("cursos/", listado_cursos),
    path('coder/', include('AppCoder.urls')),
]
