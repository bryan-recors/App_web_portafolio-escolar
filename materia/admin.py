from django.contrib import admin
from materia.models import Materia, Tarea, Evaluacion,TrabajoTarea,TrabajoEva

# Register your models here.
class MateriaAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_mat", "descripcion_mat")

class TareaAdmin(admin.ModelAdmin):
    list_display = ("id","titulo","descripcion_2","fecha_entrega")

class TrabajoTareaAdmin(admin.ModelAdmin):
    list_display = ("id","tarea_id","alumno_id","trabajo","completada")

class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ("id","titulo","descripcion","fecha_entrega")

class TrabajoEvaAdmin(admin.ModelAdmin):
    list_display = ("id","evaluacion_id","alumno_id","trabajo","completada")

admin.site.register(Materia, MateriaAdmin)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(TrabajoTarea,TrabajoTareaAdmin)
admin.site.register(Evaluacion, EvaluacionAdmin)
admin.site.register(TrabajoEva,TrabajoEvaAdmin)
