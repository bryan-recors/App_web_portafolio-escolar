from django.contrib.auth.models import User
from django.db import models
from materia.models import Materia
# Create your models here.
class Docente(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    ci_doce = models.CharField(max_length=10, verbose_name="N° de Cédula")
    especialidad_doce = models.CharField(max_length=150, verbose_name="Especialidad")
    fotografia_doce = models.ImageField(upload_to='docente/', blank=True, null=True,verbose_name="Fotografía")
    docente_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, verbose_name="Materia a impartir")
    def __str__(self):
        return self.ci_doce
