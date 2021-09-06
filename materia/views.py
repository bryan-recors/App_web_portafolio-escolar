from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.http import JsonResponse
#from materia.forms import FormularioMateria
from materia.models import Materia

from .mixins import IsSuperuserMixin, ValidatePermissionRequiredMixin,TipoPermissionRequiredMixin
#para usar el LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class ListarMaterias(LoginRequiredMixin,TipoPermissionRequiredMixin,ListView):
    #permission_required = 'alumno.estudiante'
    url_redirect = reverse_lazy('login')
    model = Materia
    template_name = 'materia/listar_materias.html'
