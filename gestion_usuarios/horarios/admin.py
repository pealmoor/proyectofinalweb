from django.contrib import admin
from .models import Horario

from django.contrib import admin
from .models import Horario

class HorarioAdmin(admin.ModelAdmin):
    list_display = ('materia', 'get_estudiantes', 'dia', 'hora_inicio', 'hora_fin', 'salon', 'profesor')

    def get_estudiantes(self, obj):
        return ", ".join([estudiante.nombre for estudiante in obj.estudiantes.all()])
    get_estudiantes.short_description = 'Estudiantes'  # Etiqueta para mostrar en el admin

admin.site.register(Horario, HorarioAdmin)

