from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Alumno(models.Model):
    CHOICES = (
        ('masculio', 'Masculino'),
        ('femenino', 'Femenino'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    ci_alu = models.CharField(max_length= 10,verbose_name="N° de Cedula")
    sexo = models.CharField(max_length=100, blank=True, choices=CHOICES, null=True)
    direccion_alu = models.CharField(max_length= 100,verbose_name="Dirección")
    email_personal_alu = models.EmailField(verbose_name="Email Personal")
    fotografia_alu = models.ImageField(upload_to='alumno/', blank=True, null=True,verbose_name="Fotografía")
    def __str__(self):
        return self.user.first_name
    class Meta:
        permissions = (
            ('estudiante', 'Permiso de estudiante'),
            ('profesor', 'Permiso de profesor'),
        )

class Anio_Lectivo(models.Model):
    fecha_inico_anio = models.DateField(verbose_name="Fecha de Inicio del Año Lectivo")
    fecha_final_anio = models.DateField(verbose_name="Fecha de Fin del Año Lectivo")

class Grado(models.Model):
    nombre_grado = models.CharField(max_length=20, verbose_name="Grado")
    def __str__(self):
        return self.nombre_grado

class Paralelo(models.Model):
    nombre_paralelo = models.CharField(max_length=10, verbose_name="Paralelo")
    paralelo_grado = models.ForeignKey(Grado, on_delete=models.CASCADE, verbose_name="Grado")
    def __str__(self):
        return self.nombre_paralelo

class Matricula(models.Model):
    fecha_matricula = models.DateField(verbose_name="Fecha de Matrícula")
    matricula_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, verbose_name="Alumno con cédula")
    matricula_anio_lectivo = models.ForeignKey(Anio_Lectivo, on_delete=models.CASCADE, verbose_name="Año Lectivo")
    matricula_grado = models.ForeignKey(Grado, on_delete=models.CASCADE, verbose_name="Grado")
    matricula_paraleo = models.ForeignKey(Paralelo, on_delete=models.CASCADE, verbose_name="Paralelo")
