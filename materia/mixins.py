from django.shortcuts import redirect
from datetime import datetime
from django.urls import reverse_lazy
#otra que puedo usar para redirigir
from django.http import HttpResponseRedirect
from django.contrib import messages

class IsSuperuserMixin(object):
    def dispatch(self,request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request,*args, **kwargs)
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_now']= datetime.now()
        return context

class ValidatePermissionRequiredMixin(object):
    #permiso
    permission_required = ''
    #url de retorno
    url_redirect = None
    #valido si tiene uno o varios permisos
    def get_perms(self):
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required
        return perms

    #validar si el usuario indica una url de redireccion
    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('login')
        return self.url_redirect

   #valido si son los permisos que requiero
    def dispatch(self,request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request,*args, **kwargs)
        messages.error(request,'No tienes Permiso para acceder a este formulario')
        return HttpResponseRedirect(self.get_url_redirect())

class TipoPermissionRequiredMixin(object):
    def dispatch(self,request, *args, **kwargs):
        if request.user.has_perm('alumno.profesor'):
            messages.success(request,'hola profesor')
            return super().dispatch(request,*args, **kwargs)
        elif request.user.has_perm('alumno.estudiante'):
            messages.success(request,'hola estudiante')
            return super().dispatch(request,*args, **kwargs)
        messages.error(request,'No tienes Permiso de profesor')
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_now']= datetime.now()
        return context
