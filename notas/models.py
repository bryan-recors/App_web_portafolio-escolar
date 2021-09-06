from django.db import models
from materia.models import Materia
from alumno.models import Alumno
# Create your models here.

class Nota(models.Model):
    nota_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, verbose_name="Materia")
    alumno_id = models.ForeignKey(Alumno, on_delete=models.CASCADE,verbose_name="Alumno con cédula")
    tarea1_not = models.FloatField(blank=True, null=True,verbose_name="Nota de Tarea 1")
    tarea2_not = models.FloatField(blank=True, null=True,verbose_name="Nota de Tarea 2")
    tarea3_not = models.FloatField(blank=True, null=True,verbose_name="Nota de Tarea 3")
    tarea4_not = models.FloatField(blank=True, null=True,verbose_name="Nota de Tarea 4")
    tarea5_not = models.FloatField(blank=True, null=True,verbose_name="Nota de Tarea 5")
    tarea6_not = models.FloatField(blank=True, null=True,verbose_name="Nota de Tarea 6")
    tarea7_not = models.FloatField(blank=True, null=True,verbose_name="Nota de Tarea 7")
    tarea8_not = models.FloatField(blank=True, null=True,verbose_name="Nota de Tarea 8")
    evaluacion1_not = models.FloatField(blank=True, null=True,verbose_name="Nota de Evaluación 1")
    evaluacion2_not = models.FloatField(blank=True, null=True,verbose_name="Nota de Evaluación 2")
    final_nota = models.FloatField(blank=True, null=True,verbose_name="Nota de Final obtenida")
    observaciones_not = models.CharField(blank=True, null=True,max_length=30, verbose_name="Observaciones")
    created_at = models.DateTimeField(auto_now_add=True)
