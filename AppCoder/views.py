from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.forms import *
from AppCoder.models import *

#Para abrir usando rutas relativas
from proyectocoder.settings import BASE_DIR
import os

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def test(request):
    ruta = os.path.join(BASE_DIR,"AppCoder/templates/AppCoder/base.html") #tengo la ruta al template para usar donde quiera
    print(BASE_DIR,__file__)
    file = open(ruta)
    return HttpResponse(file.read())

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    errores=""
    #Validamos tipo de petición
    if request.method == "POST":
        #Cargamos los datos en el formulario
        miFormulario = CursoFormulario(request.POST)
        #Validamos los datos:
        if miFormulario.is_valid():
            #Recuperamos los datos limpios:
            data = miFormulario.cleaned_data
            #Creamos el curso
            miCurso = Curso(nombre = data["nombre"], camada = data["camada"])
            #Lo guardamos en la base de datos
            miCurso.save()
        else:
            #Si el formulario no es válido guardamos los errores para mostrarlos
            errores = miFormulario.errors

    #Recuperamos todos los cursos de la base de datos
    cursos = Curso.objects.all()

    #Creamos formulario vacío
    miFormulario = CursoFormulario() #cuando crea el nuevo curso le pasa al template un formulario vacío para que se vacíen los campos
    
    #Creamos el contexto
    contexto = {"listado_cursos": cursos, "formulario": miFormulario, "errores": errores}
    
    #Retornamos la respuesta
    return render(request, "AppCoder/cursos.html", contexto) 
    
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

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id) #no usamos método filter porque devuelve una lista y solo quiero un objeto
    curso.delete()
    return redirect("coder-cursos")

def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            curso.nombre = data["nombre"]
            curso.camada = data["camada"]
            curso.save()
            return redirect("coder-cursos")
        else:
            return render(request, "AppCoder/editar_curso.html",{"formulario": miFormulario, "errores": miFormulario.errors})
    else:
        miFormulario = CursoFormulario(initial={"nombre": curso.nombre, "camada": curso.camada})
        return render(request, "AppCoder/editar_curso.html",{"formulario": miFormulario, "errores": ""})

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
    entregables = Entregable.objects.all()
    contexto = {"listado_entregables": entregables}
    return render(request, "AppCoder/entregables.html", contexto)

def listado_cursos(request):
    cursos = Curso.objects.all()

    cadena_respuesta = ""
    cadena_respuesta_2 = ""
    for curso in cursos:
        cadena_respuesta += curso.nombre + " | "
        cadena_respuesta_2 += f"({curso.nombre},{curso.camada})" + " | "
    #return HttpResponse(cadena_respuesta_2)
    #return HttpResponse(curso) se imprime como lo definí en el archivo modelo en __self__
    return HttpResponse(cursos)

class EntregablesList(ListView):
    model = Entregable
    template_name = "AppCoder/entregables.html"

class EntregableDetail(DetailView):
    model = Entregable
    template_name = "AppCoder/detalle_entregable.html"

class EntregableCreate(CreateView):
    model = Entregable
    success_url = "/coder/entregables/"
    fields = ["nombre", "fecha_de_entrega", "entregado"]
    #acepta el template_name 

class EntregableUpdate(UpdateView):
    model = Entregable
    success_url = "/coder/entregables/"
    fields = ["nombre", "fecha_de_entrega", "entregado"]
    #acepta el template_name 

class EntregableDelete(DeleteView):
    model = Entregable
    success_url = "/coder/entregables/"
    #acepta el template_name 