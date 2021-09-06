from django import forms
from materia.models import Tarea

class FormularioCrearTarea(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = Tarea
        fields = ('titulo','descripcion_2','fecha_entrega','tarea_materia')
        labels = {
            #como quiero que se vean los labels
            'titulo': 'Titulo de la Tarea',
            'descripcion_2':'Descripción',
            'fecha_entrega':'Fecha de entrega ejemplo: 2020-06-25',
            'tarea_materia': 'Seleccione la materia a la que pertenece'
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'titulo',
                }
            ),
            'descripcion_2': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripción',
                }
            ),
            'fecha_entrega': forms.DateInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'formato Año-Mes-Dia ejemplo:2020-06-25',
                }
            )
        }
