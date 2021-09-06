from django.db import models
from alumno.models import Alumno

# Create your models here.
class Materia(models.Model):
    nombre_mat = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion_mat = models.CharField(max_length=50, verbose_name="Descripción")
    alumno_id = models.ManyToManyField(Alumno, verbose_name="Alumno con cédula")
    def __str__(self):
        return self.nombre_mat

class Tarea(models.Model):
    titulo = models.CharField(max_length= 300,verbose_name="Titulo de la tarea")
    descripcion_2 = models.TextField(verbose_name="Descripcion")
    fecha_entrega = models.DateField(blank=True, null=True,verbose_name="Fecha de entrega")
    tarea_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, verbose_name="Materia")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['titulo']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.titulo

class TrabajoTarea(models.Model):
    tarea_id = models.ForeignKey(Tarea, on_delete=models.CASCADE, verbose_name="Tarea")
    alumno_id = models.ForeignKey(Alumno, on_delete=models.CASCADE,verbose_name="Alumno con cedula")
    trabajo = models.FileField(upload_to='trabajos/', blank=True, null=True)
    completada = models.BooleanField(default=False)

class Evaluacion(models.Model):
    titulo = models.CharField(max_length= 300,verbose_name="titulo de la evaluacion")
    descripcion = models.TextField(verbose_name="Descripcion")
    fecha_entrega = models.DateField(blank=True, null=True,verbose_name="Fecha de entrega")
    evaluacion_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, verbose_name="Materia")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'Evaluacion'
        verbose_name_plural = 'Evaluaciones'
        ordering = ['titulo']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.titulo

class TrabajoEva(models.Model):
    trabajo = models.FileField(upload_to='evaluaiones/', blank=True, null=True)
    evaluacion_id = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, verbose_name="Evaluacion")
    alumno_id = models.ForeignKey(Alumno, on_delete=models.CASCADE,verbose_name="Alumno con cedula")
    completada = models.BooleanField(default=False)
