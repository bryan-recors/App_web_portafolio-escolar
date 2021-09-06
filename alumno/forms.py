from django import forms
from materia.models import TrabajoTarea 

class FormularioTrabajoTarea(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = TrabajoTarea
        fields = ('tarea_id','alumno_id','trabajo','completada')
        labels = {
            #como quiero que se vean los labels
            'tarea_id': 'A que tarea pertenece',
            'alumno_id':'Que estudiante realiza',
            'trabajo':'Trabajo',
            'completada': 'Tarea realizada'
        }
        widgets = {
            'tarea_id': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Seleccione la tarea a la que corresponde ',
                }
            ),
            'alumno_id': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Seleccione el estudiante',
                }
            ),
            'trabajo': forms.FileInput(
                attrs = {
                    'placeholder': 'cargue el trabajo',
                }
            ),

            'productos': forms.CheckboxInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Seleccione los productos',
                }
            )
        }
