from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

# Create your views here.
# Vista para listar cursos
def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursosapp/cursos/lista_cursos.html', {'cursos': cursos})

# Vista para crear un curso
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursosapp/cursos/crear_curso.html', {'form': form})

# Vista para actualizar un curso
def actualizar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursosapp/cursos/actualizar_curso.html', {'form': form, 'curso': curso})

# Vista para borrar un curso
def borrar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        curso.delete()
        return redirect('lista_cursos')
    return render(request, 'cursosapp/cursos/borrar_curso.html', {'curso': curso})


# Vista para listar estudiantes
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'cursosapp/estudiantes/lista_estudiantes.html', {'estudiantes': estudiantes})

# Vista para crear un estudiante
def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'cursosapp/estudiantes/crear_estudiante.html', {'form': form})

# Vista para actualizar un estudiante
def actualizar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'cursosapp/estudiantes/actualizar_estudiante.html', {'form': form, 'estudiante': estudiante})

# Vista para borrar un estudiante
def borrar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('lista_estudiantes')
    return render(request, 'cursosapp/estudiantes/borrar_estudiante.html', {'estudiante': estudiante})

# Vista para listar inscripciones
def lista_inscripciones(request):
    inscripciones = Inscripcion.objects.select_related('estudiante', 'curso')
    return render(request, 'cursosapp/inscripciones/lista_inscripciones.html', {'inscripciones': inscripciones})

# Vista para crear una inscripción
def crear_inscripcion(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_inscripciones')
    else:
        form = InscripcionForm()
    return render(request, 'cursosapp/inscripciones/crear_inscripcion.html', {'form': form})

# Vista para actualizar una inscripción
def actualizar_inscripcion(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id)
    if request.method == 'POST':
        form = InscripcionForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('lista_inscripciones')
    else:
        form = InscripcionForm(instance=inscripcion)
    return render(request, 'cursosapp/inscripciones/actualizar_inscripcion.html', {'form': form, 'inscripcion': inscripcion})

# Vista para borrar una inscripción
def borrar_inscripcion(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('lista_inscripciones')
    return render(request, 'cursosapp/inscripciones/borrar_inscripcion.html', {'inscripcion': inscripcion})
