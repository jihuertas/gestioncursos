from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class cursos(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    fechaInicio = models.DateField(blank=True, null=True)
    fechaFin = models.DateField(blank=True, null=True)

    class Meta():
        verbose_name = "curso"
        verbose_name_plural = "cursos"
    
    def __str__(self):
        return self.nombre
    
    def clean(self):
        cleaned_data = super().clean()
        if self.fechaInicio and self.fechaFin and self.fechaInicio > self.fechaFin:
            raise ValidationError("La fecha de inicio no puede ser superior a la fecha de fin")
        return super().clean() 


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(null=True)

