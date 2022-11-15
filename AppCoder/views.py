from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import *
from AppCoder.models import *

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")
    
def crear_curso(request):
    if request.method == "POST":
        nombre_curso = request.POST["curso"]
        numero_camada = request.POST["camada"]
        
        curso = Curso(nombre = nombre_curso,camada = numero_camada)
        curso.save()

        return render(request, "AppCoder/inicio.html") #cuando crea curso nuevo me lleva a la página de inicio

    return render(request, "AppCoder/curso_formulario.html")

def buscar_curso(request):
    return render(request, "AppCoder/busqueda_cursos.html")

def resultados_buscar_cursos(request):
    nombre_curso = request.GET["nombre_curso"]
    cursos = Curso.objects.filter(nombre__icontains=nombre_curso)
    return render(request, "AppCoder/resultados_busqueda_cursos.html", {"cursos": cursos})

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def crear_profesor(request):
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            miProfesor = Profesor(nombre = miFormulario.cleaned_data["nombre"], apellido = miFormulario.cleaned_data["apellido"], email = miFormulario.cleaned_data["email"], profesion = miFormulario.cleaned_data["profesion"])
            miProfesor.save()
    miFormulario = ProfesorFormulario() #cuando crea el nuevo profesor le pasa al template un formulario vacío para que se vacíen los campos
    contexto = {"formulario": miFormulario}
    return render(request, "AppCoder/profesores_formulario.html", contexto)

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def listado_cursos(request):
    cursos = Curso.objects.all()

    cadena_respuesta = ""
    cadena_respuesta_2 = ""
    for curso in cursos:
        cadena_respuesta += curso.nombre + " | "
        cadena_respuesta_2 += f"({curso.nombre},{curso.camada})" + " | "
    #return HttpResponse(cadena_respuesta_2)
    return HttpResponse(cadena_respuesta_2)