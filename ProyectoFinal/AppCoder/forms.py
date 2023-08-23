from django import forms
class CursoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    comision=forms.IntegerField()
    
class ProfesorForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=50)

class ConsejeroEscolarForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    correo = forms.EmailField()
    tiene_experiencia = forms.BooleanField(initial=False, required=False)
    telefono = forms.CharField(max_length=9) 
class BibliotecarioForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    correo = forms.EmailField()
    numero_identificacion = forms.CharField(max_length=7)
    cargo = forms.CharField(max_length=50)
    
class EstudianteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email= forms.EmailField()

class EntregableForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    fecha_entrega= forms.DateField()
    entregado= forms.BooleanField()
