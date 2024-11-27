from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_electronico = models.EmailField(unique=True)
    direccion = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    programa = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.programa}"
