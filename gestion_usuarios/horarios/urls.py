# horarios/urls.py
from django.urls import path
from .views import HorarioEstudianteListView, HorarioProfesorListView

urlpatterns = [
    path('horarios/estudiante/', HorarioEstudianteListView.as_view(), name='horarios_estudiante'),
    path('horarios/profesor/', HorarioProfesorListView.as_view(), name='horarios_profesor'),
]
