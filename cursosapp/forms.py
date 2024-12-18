from django import forms
from .models import *
from django.core.exceptions import ValidationError

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'codigo', 'fecha_inicio', 'fecha_fin']
        widgets = {'fecha_inicio':forms.DateInput(format='%Y-%m-%d',attrs={'type':'date'}),
                    'fecha_fin':forms.DateInput(format='%Y-%m-%d',attrs={'type':'date'})}

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin and fecha_inicio >= fecha_fin:
            raise ValidationError("La fecha de inicio debe ser anterior a la fecha de finalización.")


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'email', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date'})
        }

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento > date.today():
            raise ValidationError("La fecha de nacimiento no puede ser futura.")
        edad = (date.today() - fecha_nacimiento).days // 365
        if edad < 18:
            raise ValidationError("El estudiante debe tener al menos 18 años.")
        return fecha_nacimiento


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['estudiante', 'curso', 'fecha_inscripcion']
        widgets = {
            'fecha_inscripcion': forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date'})
        }

    def clean(self):
        cleaned_data = super().clean()
        curso = cleaned_data.get('curso')
        estudiante = cleaned_data.get('estudiante')
        fecha_inscripcion = cleaned_data.get('fecha_inscripcion')

        if fecha_inscripcion and curso and fecha_inscripcion > curso.fecha_fin:
            raise ValidationError("No se puede inscribir a un curso que ya ha finalizado.")
        
        if estudiante and curso:
            # Evitar inscripciones duplicadas, exceptuando la actual
            instance_id = self.instance.id if self.instance else None
            if Inscripcion.objects.filter(estudiante=estudiante, curso=curso).exclude(id=instance_id).exists():
                raise ValidationError("El estudiante ya está inscrito en este curso.")

        return cleaned_data
