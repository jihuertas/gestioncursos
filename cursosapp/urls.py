
from django.urls import path
from .views import *

urlpatterns = [
    #path('cursos/', lista_cursos, name='lista_cursos'),
    path('cursos/', ListarCursos.as_view(), name='lista_cursos'),
    #path('cursos/crear/', crear_curso, name='crear_curso'),
    path('cursos/crear/', CrearCurso.as_view(), name='crear_curso'),
    #path('cursos/<int:curso_id>/editar/', actualizar_curso, name='actualizar_curso'),
    path('cursos/<int:curso_id>/editar/', ActualizarCurso.as_view(), name='actualizar_curso'),
    #path('cursos/<int:curso_id>/borrar/', borrar_curso, name='borrar_curso'),
    path('cursos/<int:curso_id>/borrar/', BorrarCurso.as_view(), name='borrar_curso'),
   
    path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/crear/', crear_estudiante, name='crear_estudiante'),
    path('estudiantes/<int:estudiante_id>/editar/', actualizar_estudiante, name='actualizar_estudiante'),
    path('estudiantes/<int:estudiante_id>/borrar/', borrar_estudiante, name='borrar_estudiante'),
    
    path('inscripciones/', lista_inscripciones, name='lista_inscripciones'),
    path('inscripciones/crear/', crear_inscripcion, name='crear_inscripcion'),
    path('inscripciones/<int:inscripcion_id>/editar/', actualizar_inscripcion, name='actualizar_inscripcion'),
    path('inscripciones/<int:inscripcion_id>/borrar/', borrar_inscripcion, name='borrar_inscripcion'),

]

