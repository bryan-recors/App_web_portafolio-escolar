from django.urls import path
from django.contrib.auth.decorators import login_required
from docente.views import  DocenteMateriasDetailView,DocenteTareasDetailView,CrearTarea,TrabajosDetailView

urlpatterns = [
    path('docente_materias/',login_required(DocenteMateriasDetailView.as_view()), name ='docente_materias'),
    path('ver_tareas/<pk>',login_required(DocenteTareasDetailView.as_view()), name ='ver_tareas'),
    path('crear_tarea/',login_required(CrearTarea.as_view()),name ='crear_tarea'),
    path('ver_trabajos/<pk>',login_required(TrabajosDetailView.as_view()),name ='ver_trabajos'),
]
