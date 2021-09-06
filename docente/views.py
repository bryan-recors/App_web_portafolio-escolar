from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from materia.models import Materia,Tarea,TrabajoTarea
from docente.models import Docente
from django.shortcuts import render
from django.urls import reverse_lazy
from docente.forms import FormularioCrearTarea

class HomeDocente(TemplateView):
    template_name = 'docente/home_docente.html'

class DocenteMateriasDetailView(ListView):
    model = Materia
    template_name = 'docente/mis_materias_docente.html'

    def get_queryset(self):
        return Materia.objects.filter(docente__id=self.get_object())

    def dispatch(self,request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request,*args, **kwargs)

    def get_object(self, queryset=None):
        docente=self.request.user.docente.id
        print(docente)
        return self.request.user.docente.id

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class DocenteTareasDetailView(ListView):
    model = Tarea
    template_name = 'docente/docente_tareas.html'

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


class TrabajosDetailView(ListView):
    model = TrabajoTarea
    template_name = 'docente/ver_trabajos.html'

    def get_queryset(self):
        return TrabajoTarea.objects.filter(tarea_id_id=self.get_object())

    def dispatch(self,request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request,*args, **kwargs)

    def get_object(self, queryset=None):
        obj = Tarea.objects.get(id=self.kwargs['pk'])
        tarea= obj.id
        print(tarea)
        return tarea

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class CrearTarea(CreateView):
    model = Tarea
    form_class = FormularioCrearTarea
    template_name = 'docente/crear_tarea.html'
    success_url = reverse_lazy('docente:docente_materias')
