from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.

def listado_cursos(request):
    cursos = Curso.objects.all()

    cadena_respuesta = ""
    cadena_respuesta_2 = ""
    for curso in cursos:
        cadena_respuesta += curso.nombre + " | "
        cadena_respuesta_2 += f"({curso.nombre},{curso.camada})" + " | "
    #return HttpResponse(cadena_respuesta_2)
    return HttpResponse(cadena_respuesta_2)