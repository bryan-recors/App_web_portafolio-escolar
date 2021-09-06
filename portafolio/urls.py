from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .import views
from alumno.views import HomeEstudiante
from docente.views import HomeDocente
urlpatterns = [
    #path('usuarios/',include(('usuario.urls','usuarios'))),
    path('',views.index, name= 'index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout/',views.logout_view, name= 'logout'),
    path('admin/', admin.site.urls),
    #********************** ruta de alumnos****************
    path('alumno/',include(('alumno.urls','alumno'))),
    path('estudiante/', HomeEstudiante.as_view(),name ='home_estudiante'),
    #********************** ruta de docente****************
    path('docente/',include(('docente.urls','docente'))),
    path('docente/', HomeDocente.as_view(),name ='home_docente'),
    #********************** ruta de la app materias****************
    path('materia/',include(('materia.urls','materia'))),

]
#si los modelos tienen imagenes o documentos
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
