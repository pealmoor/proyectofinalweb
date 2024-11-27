from django.contrib import admin
from .models import Profesor

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'programa', 'correo_electronico')
    search_fields = ('nombre', 'apellido', 'programa')
