from django import forms   

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=100)