# En estudiantes/models.py
from django.db import models
from profesores.models import Profesor

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name="materias")
    creditos = models.PositiveSmallIntegerField()
    nota = models.FloatField(null=True, blank=True)
    
    # Relacionamos estudiantes sin importar el modelo directamente
    estudiantes = models.ManyToManyField('estudiantes.Estudiante', related_name="materias_matriculadas")

    def __str__(self):
        return self.nombre
        
class Horario(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    dia = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    salon = models.CharField(max_length=50)
