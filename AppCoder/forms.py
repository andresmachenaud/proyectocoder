from django import forms   

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=100)

class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    camada = forms.IntegerField(min_value=10000) #validación de datos de nuevo curso al menos 5 cifras el num de camada