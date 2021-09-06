from django.contrib import admin
from alumno.models import Alumno, Anio_Lectivo, Grado, Paralelo, Matricula
# Register your models here.

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("user","ci_alu", "sexo","direccion_alu")

class Anio_LectivoAdmin(admin.ModelAdmin):
    list_display = ("id","fecha_inico_anio", "fecha_final_anio")

class GradoAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_grado",)

class ParaleloAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_paralelo", "paralelo_grado")

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ("id","fecha_matricula", "matricula_alumno", "matricula_anio_lectivo", "matricula_grado", "matricula_paraleo")

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Anio_Lectivo, Anio_LectivoAdmin)
admin.site.register(Grado, GradoAdmin)
admin.site.register(Paralelo, ParaleloAdmin)
admin.site.register(Matricula, MatriculaAdmin)
