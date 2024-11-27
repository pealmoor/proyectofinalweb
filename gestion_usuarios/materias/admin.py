from django.contrib import admin
from .models import Materia
from .models import Horario

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'profesor', 'creditos', 'nota')
    search_fields = ('nombre', 'profesor__nombre')

class HorarioAdmin(admin.ModelAdmin):
    list_display = ('materia', 'dia', 'hora_inicio', 'hora_fin', 'salon', 'get_profesor')

    def get_profesor(self, obj):
        return obj.profesor.nombre  # Asumiendo que tienes un campo 'nombre' en el modelo Profesor
    get_profesor.short_description = 'Profesor'  # Para que se muestre como 'Profesor' en el admin

admin.site.register(Horario, HorarioAdmin)