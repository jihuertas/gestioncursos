from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Curso, Estudiante, Inscripcion

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = Estudiante
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('foto', 'fecha_nacimiento')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('foto', 'fecha_nacimiento')}),
    )


admin.site.register(Curso)
admin.site.register(Estudiante,CustomUserAdmin)
admin.site.register(Inscripcion)