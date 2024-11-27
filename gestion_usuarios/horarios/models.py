from django.db import models
from materias.models import Materia
from estudiantes.models import Estudiante
from profesores.models import Profesor

# En el modelo Horario
# En el modelo Horario
class Horario(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='horarios')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='horarios_profesor')
    estudiantes = models.ManyToManyField(Estudiante, related_name='horarios')
    dia = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    salon = models.CharField(max_length=50)



    def __str__(self):
        return f"{self.materia.nombre} - {self.dia} {self.hora_inicio}-{self.hora_fin} - {self.salon}"
