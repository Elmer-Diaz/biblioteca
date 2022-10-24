from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from apps.usuario.models import Usuario


class FormularioUsuario(forms.ModelForm):

    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput(
        attrs= {
            'class' : 'form-control',
            'placeholder' : 'Ingrese su contraseña',
            'id' : 'password1',
            'required': 'required',

        }
    ))

    password2 = forms.CharField(label='Contraseña de confirmación', widget= forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente su contraseña',
            'id': 'password2',
            'required': 'required',

        }
    ))

    class Meta:
        model = Usuario
        fields = ('email', 'username', 'nombres', 'apellidos', 'imagen')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo Electrónico',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus nombres',
                    'autocomplete': 'off'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos',
                    'autocomplete': 'off'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre de usuario',
                    'autocomplete': 'off'
                }
            )
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2
    
    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user
        
        