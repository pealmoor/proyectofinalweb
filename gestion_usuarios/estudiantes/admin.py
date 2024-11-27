from django.contrib import admin
from .models import Estudiante

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'codigo_estudiante', 'carrera', 'semestre', 'promedio')
    search_fields = ('nombre', 'apellido', 'codigo_estudiante')
