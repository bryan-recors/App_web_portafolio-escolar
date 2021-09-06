from django.contrib import admin
from notas.models import Nota
# Register your models here.
class NotaAdmin(admin.ModelAdmin):
    list_display = ("id","nota_materia", "alumno_id","tarea1_not", "tarea2_not", "tarea3_not", "tarea4_not", "tarea5_not", "tarea6_not", "tarea7_not", "tarea8_not", "evaluacion1_not", "evaluacion2_not", "final_nota", "observaciones_not")

admin.site.register(Nota, NotaAdmin)
