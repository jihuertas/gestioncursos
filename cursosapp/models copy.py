from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()


    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

    def clean(self):
        if self.fecha_inicio >= self.fecha_fin:
            raise ValidationError("La fecha de inicio debe ser anterior a la fecha de finalización.")

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

    def clean(self):
        if self.fecha_nacimiento > date.today():
            raise ValidationError("La fecha de nacimiento no puede ser futura.")
        edad = (date.today() - self.fecha_nacimiento).days // 365
        if edad < 18:
            raise ValidationError("El estudiante debe tener al menos 18 años.")


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="inscripciones")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="inscripciones")
    fecha_inscripcion = models.DateField()

    def __str__(self):
        return f"{self.estudiante.nombre} inscrito en {self.curso.nombre}"

    def clean(self):
        if self.fecha_inscripcion > date.today():
            raise ValidationError("La fecha de inscripción no puede ser futura.")
        if self.fecha_inscripcion > self.curso.fecha_fin:
            raise ValidationError("No se puede inscribir a un curso que ya ha finalizado.")
        
        # Validación para evitar inscripciones duplicadas
        if Inscripcion.objects.filter(estudiante=self.estudiante, curso=self.curso).exclude(id=self.id).exists():
            raise ValidationError("El estudiante ya está inscrito en este curso.")

