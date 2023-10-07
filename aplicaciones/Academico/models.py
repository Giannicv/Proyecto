from django.db import models

# Create your models here.

class Alumno(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    nota = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"



