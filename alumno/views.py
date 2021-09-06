from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from materia.models import Materia,Tarea,TrabajoTarea
from alumno.models import Alumno
from django.shortcuts import render
from alumno.forms import FormularioTrabajoTarea
from django.urls import reverse_lazy

class HomeEstudiante(TemplateView):
    template_name = 'alumno/home_estudiante.html'

class MateriasDetailView(ListView):
    model = Materia
    template_name = 'alumno/mis_materias.html'

    def get_queryset(self):
        return Materia.objects.filter(alumno_id__id=self.get_object())

    def dispatch(self,request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request,*args, **kwargs)

    def get_object(self, queryset=None):
        alumno=self.request.user.alumno.id
        print(alumno)
        return self.request.user.alumno.id

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class TareasDetailView(ListView):
    model = Tarea
    template_name = 'alumno/mis_tareas.html'

    def get_queryset(self):
        return Tarea.objects.filter(tarea_materia_id=self.get_object())

    def dispatch(self,request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request,*args, **kwargs)

    def get_object(self, queryset=None):
        obj = Materia.objects.get(id=self.kwargs['pk'])
        materia= obj.id
        print(materia)
        return materia

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class RegistrarTrabajoTarea(CreateView):
    model = TrabajoTarea
    form_class = FormularioTrabajoTarea
    template_name = 'alumno/entregar_tarea.html'
    success_url = reverse_lazy('alumno:mis_materias')



"""
class MateriasDetailView(ListView):
    model = Materia
    template_name = 'materia/listar_materias.html'
    consulta = Materia.objects.all()
    print(consulta)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
"""
