from django.contrib import admin
from docente.models import Docente

class DocenteAdmin(admin.ModelAdmin):
    list_display = ("user","ci_doce","especialidad_doce","docente_materia")
admin.site.register(Docente, DocenteAdmin)
