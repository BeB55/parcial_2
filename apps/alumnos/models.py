from django.db import models
from django.contrib.auth.models import User

class Alumno(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # cada usuario maneja sus alumnos
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    curso = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
