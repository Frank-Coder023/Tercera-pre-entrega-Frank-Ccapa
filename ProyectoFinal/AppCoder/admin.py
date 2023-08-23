from django.contrib import admin
from .models import Curso,Entregable, Estudiante, Profesor, Bibliotecario, ConsejeroEscolar
# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)
admin.site.register(Bibliotecario)
admin.site.register(ConsejeroEscolar)