from django.urls import path
from django.contrib.auth.decorators import login_required
from alumno.views import  MateriasDetailView,TareasDetailView,RegistrarTrabajoTarea
urlpatterns = [
    path('mis_materias/',login_required(MateriasDetailView.as_view()), name ='mis_materias'),
    path('mis_tareas/<pk>',login_required(TareasDetailView.as_view()), name ='mis_tareas'),
    path('entregar_trabajo/',login_required(RegistrarTrabajoTarea.as_view()),name ='entregar_trabajos'),
]
