from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True, label="Cuenta de Correo")
    profesion = forms.CharField(max_length=50, required=True)

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    comision = forms.IntegerField(required=True)


class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



