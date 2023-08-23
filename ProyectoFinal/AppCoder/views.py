from django.shortcuts import render
from .models import Curso, Profesor, ConsejeroEscolar, Bibliotecario, Estudiante, Entregable
from django.http import HttpResponse
from .forms import CursoForm, ProfesorForm, ConsejeroEscolarForm, BibliotecarioForm, EstudianteForm, EntregableForm
# Create your views here.
def crear_curso(request):
    nombre_curso="Programacion Basica"
    comision_curso=999888
    print("creando curso")
    curso=Curso(nombre=nombre_curso,comision=comision_curso)
    curso.save()
    respuesta=f"Curso creado: {curso.nombre} - {curso.comision}"
    return HttpResponse(respuesta)
def listar_cursos(request):
    cursos=Curso.objects.all()
    respuesta=""
    for curso in cursos:
        respuesta+=f"{curso.nombre} - {curso.comision}<br>"
    return HttpResponse(respuesta)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def profesores(request):
    if request.method=="POST":
        form=ProfesorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            profesion=info["profesion"]
            profesor=Profesor(nombre=nombre,apellido=apellido,email=email,profesion=profesion)
            profesor.save()
            formulario_profesor=ProfesorForm()
            return render(request,"AppCoder/profesores.html", {"mensaje":"Profesor creado", "formulario":formulario_profesor})
        else:
            return render(request,"AppCoder/profesores.html", {"mensaje":"Datos invalidos"})
    else:

        formulario_profesor=ProfesorForm()

    return render(request,"AppCoder/profesores.html", {"formulario":formulario_profesor})

def estudiantes(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            email = info["email"]
            estudiante = Estudiante(nombre=nombre, apellido=apellido, email=email)
            estudiante.save()
            formulario_estudiante = EstudianteForm()
            return render(request, "AppCoder/estudiantes.html", {"mensaje": "Estudiante creado", "formulario": formulario_estudiante})
        else:
            return render(request, "AppCoder/estudiantes.html", {"mensaje": "Datos inválidos"})
    else:
        formulario_estudiante = EstudianteForm()
    
    return render(request, "AppCoder/estudiantes.html", {"formulario": formulario_estudiante})



def entregables(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            fecha_entrega = info["fecha_entrega"]
            entregado = info["entregado"]
            entregable = Entregable(nombre=nombre, fecha_entrega=fecha_entrega, entregado=entregado)
            entregable.save()
            
            formulario_entregable = EntregableForm()
            return render(request, "AppCoder/entregables.html", {"mensaje": "Entregable creado", "formulario": formulario_entregable})
        else:
            return render(request, "AppCoder/entregables.html", {"mensaje": "Datos inválidos"})
    else:
        formulario_entregable = EntregableForm()
    
    return render(request, "AppCoder/entregables.html", {"formulario": formulario_entregable})

def cursos(request):
    if request.method=="POST":
        form=CursoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            comision=info["comision"]
            curso=Curso(nombre=nombre,comision=comision)
            curso.save()
            formulario_curso=CursoForm()
            return render(request,"AppCoder/cursos.html", {"mensaje":"Curso creado"})
        return render(request,"AppCoder/cursos.html", {"mensaje":"Datos invalidos"})
    else:
        formulario_curso=CursoForm()
        return render(request, "AppCoder/cursos.html", {"formulario":formulario_curso})
def busquedaComision(request):
    return render(request,"AppCoder/busquedaComision.html")

def buscar2(request):
    comision=request.GET["comision"]
    if comision!="":
        cursos=Curso.objects.filter(comision__icontains=comision)
        return render(request,"AppCoder/resultadosBusqueda.html", {"cursos":cursos})
    else:
        return render(request,"AppCoder/busquedaComision.html", {"mensaje":"che! no me ingresaste nada!!"})
    
def buscar(request):
    comision = request.GET.get("comision")
    cursos = None

    if comision:
        cursos = Curso.objects.filter(comision__icontains=comision)

    return render(request, "AppCoder/inicio.html", {"cursos": cursos, "comision": comision})


def consejeroEscolar(request):
    if request.method == 'POST':
        form = ConsejeroEscolarForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            correo = info["correo"]
            tiene_experiencia = info["tiene_experiencia"]
            telefono = info["telefono"]
            consejero = ConsejeroEscolar(nombre=nombre, apellido=apellido, correo=correo, tiene_experiencia=tiene_experiencia, telefono=telefono)
            consejero.save()
            formulario_consejero = ConsejeroEscolarForm()
            return render(request, "AppCoder/consejeroEscolar.html", {"mensaje": "Consejero escolar creado", "formulario": formulario_consejero})
        else:
            return render(request, "AppCoder/consejeroEscolar.html", {"mensaje": "Datos inválidos"})
    else:
        formulario_consejero = ConsejeroEscolarForm()

    return render(request, "AppCoder/consejeroEscolar.html", {"formulario": formulario_consejero})


def bibliotecarios(request):
    if request.method == 'POST':
        form = BibliotecarioForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            correo = info["correo"]
            numero_identificacion = info["numero_identificacion"]
            cargo = info["cargo"]
            bibliotecario = Bibliotecario(nombre=nombre, apellido=apellido, correo=correo, numero_identificacion=numero_identificacion, cargo=cargo)
            bibliotecario.save()
            
            formulario_bibliotecario = BibliotecarioForm()
            return render(request, "AppCoder/bibliotecarios.html", {"mensaje": "Bibliotecario creado", "formulario": formulario_bibliotecario})
        else:
            return render(request, "AppCoder/bibliotecarios.html", {"mensaje": "Datos inválidos"})
    else:
        formulario_bibliotecario = BibliotecarioForm()
    
    return render(request, "AppCoder/bibliotecarios.html", {"formulario": formulario_bibliotecario})

def busquedaPersonas(request):
    nombre = request.GET.get("nombre")
    resultados = []
    
    if nombre:
        resultados_profesores = Profesor.objects.filter(nombre__icontains=nombre)
        resultados_bibliotecarios = Bibliotecario.objects.filter(nombre__icontains=nombre)
        resultados_estudiantes = Estudiante.objects.filter(nombre__icontains=nombre)
        resultados_consejeros = ConsejeroEscolar.objects.filter(nombre__icontains=nombre)
        
        for resultado in resultados_profesores:
            resultados.append({"tipo": "Profesor", "nombre": resultado.nombre, "apellido": resultado.apellido})
        
        for resultado in resultados_bibliotecarios:
            resultados.append({"tipo": "Bibliotecario", "nombre": resultado.nombre, "apellido": resultado.apellido})
        
        for resultado in resultados_estudiantes:
            resultados.append({"tipo": "Estudiante", "nombre": resultado.nombre, "apellido": resultado.apellido})
        
        for resultado in resultados_consejeros:
            resultados.append({"tipo": "Consejero Escolar", "nombre": resultado.nombre, "apellido": resultado.apellido})
    
    return render(request, "AppCoder/inicio.html", {"resultados": resultados})