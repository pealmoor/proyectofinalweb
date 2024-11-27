from django.db import models
from materias.models import Materia

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_electronico = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    codigo_estudiante = models.CharField(max_length=15, unique=True)
    carrera = models.CharField(max_length=100)
    semestre = models.PositiveSmallIntegerField()
    promedio = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.codigo_estudiante}"

def calcular_promedio(self):
        # Obtenemos todas las materias matriculadas por este estudiante
        materias = self.materias_matriculadas.all()

        # Sumamos las notas de todas las materias (si existen)
        total_notas = sum(materia.nota for materia in materias if materia.nota is not None)

        # Contamos cuántas materias tienen nota asignada
        cantidad_materias = sum(1 for materia in materias if materia.nota is not None)

        if cantidad_materias > 0:
            self.promedio = total_notas / cantidad_materias
        else:
            self.promedio = 0.0  # Si no hay notas, el promedio es 0

        # Guardamos el promedio calculado
        self.save()

    
def save(self, *args, **kwargs):
    self.calcular_promedio()
    super().save(*args, **kwargs)
