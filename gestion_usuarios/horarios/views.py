# horarios/views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import Profesor, Horario
from estudiantes.models import Estudiante
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class HorarioEstudianteListView(ListView):
    model = Horario
    template_name = 'horarios/horario_estudiante.html'
    context_object_name = 'horarios'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        # Filtra los horarios según el estudiante logueado
        estudiante = Estudiante.objects.get(user=self.request.user)
        return Horario.objects.filter(estudiantes=estudiante)

class HorarioProfesorListView(ListView):
    model = Horario
    template_name = 'horarios/horario_profesor.html'
    context_object_name = 'horarios'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        # Filtra los horarios según el profesor logueado
        profesor = Profesor.objects.get(user=self.request.user)
        return Horario.objects.filter(profesor=profesor)
