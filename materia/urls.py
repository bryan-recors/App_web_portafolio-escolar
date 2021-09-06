from django.urls import path
#from django.contrib.auth.decorators import login_required
from materia.views import ListarMaterias

urlpatterns = [
    path('listar_materias/',ListarMaterias.as_view(),name ='listar_materias'),
]
