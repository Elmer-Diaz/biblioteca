from django.forms import *
from apps.libro.models import *

class categoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        # labels= {
        #     'name': 'Nombre'
        # }
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un nombre',
                    'autocomplete': 'off'
                }
            )
        }

class autorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Los Nombres',
                    'autocomplete': 'off'
                }
            ),
            'apellidos': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese los Apellidos',
                    'autocomplete': 'off'
                }
            ),
            'nacionalidad': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la Nacionalidad',
                    'autocomplete': 'off'
                }
            ),
            'sexo': RadioSelect(
               
            )
            
        }
        


       


class editorialForm(ModelForm):
    class Meta:
        model = Editorial
        fields = '__all__'
        widgets = {
            'nombreedi': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un nombre',
                    'autocomplete': 'off'
                }
            )
        }


class idiomaForm(ModelForm):
    class Meta:
        model = Idioma
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un nombre',
                    'autocomplete': 'off'
                }
            )
        }
    
class libroForm(ModelForm):
    class Meta:
        model = libro
        fields = '__all__'
        widgets = {
            'titulo': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un nombre',
                    'autocomplete': 'off'
                }
            ),
            'fechapublicacion': DateInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese una Fecha (14/05/2000)',
                    'autocomplete': 'off'
                }
            )

        }


class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
