from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("inicio/", inicio, name="coder-inicio"),
    path("estudiantes/", estudiantes, name="coder-estudiantes"),
    path("profesores/", profesores, name="coder-profesores"),
    path("profesores/crear/", crear_profesor, name="coder-profesores-crear"),
    path("cursos/", cursos, name="coder-cursos"),
    path("cursos/crear/", crear_curso, name="coder-cursos-crearr"),
    path("cursos/buscar/", buscar_curso, name="coder-cursos-buscar"),
    path("cursos/buscar/resultados/", resultados_buscar_cursos, name="coder-cursos-buscar-resultados"),
    path("entregables/", entregables, name="coder-entregables"),
]
