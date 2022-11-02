from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader

def vista_saludo(request):
    return HttpResponse("<b>Hola Coders! :) ") #el string es un archivo html


def dia_hoy(request, nombre):
    hoy = datetime.now()

    respuesta = f"Hoy es {hoy} - Bienvenid@ {nombre}"
    return HttpResponse(respuesta)

def ano_nacimiento(request, edad):
    hoy = datetime.now()
    edad = int(edad)
    año = hoy.year-edad 
    respuesta = f"Tu año de nacimiento es {año}"
    return HttpResponse(respuesta)

def vista_plantilla_bonita(request):
    archivo = open(r"C:\Users\Usuario\Desktop\Python Coderhouse\17_django\proyectocoder\proyectocoder\templates\plantilla_bonita.html")
    plantilla = Template(archivo.read()) #.read() devuelve en un solo string todo el contenido del archivo en un str
    #Template() genera un archivo del tipo template

    datos = {"Nombre": "Andrés", "Fecha":datetime.now(), "Apellido":"Macheanud"}
    contexto = Context(datos)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def vista_listado_alumnos(request):

    #Abrimos el archivo
    archivo = open(r"C:\Users\Usuario\Desktop\Python Coderhouse\17_django\proyectocoder\proyectocoder\templates\listado_alumnos.html")

    #Creamos el template
    plantilla = Template(archivo.read())

    #Cerramos el archivo para liberar contenido
    archivo.close()
    
    #Creamos el diccionario de datos
    lista_alumnos = ["Andrés Machenaud", "Leonel Gareis", "Christian García", "Agustín Russo"]
    datos = {"tecnologia": "Python", "listado_alumnos": lista_alumnos}

    contexto = Context(datos)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def vista_listado_alumnos_2(request):
    lista_alumnos = ["Andrés Machenaud", "Leonel Gareis", "Christian García", "Agustín Russo"]
    datos = {"tecnologia": "Python", "listado_alumnos": lista_alumnos}
    plantilla = loader.get_template("listado_alumnos.html")
    documento= plantilla.render(datos)
    return HttpResponse(documento)