from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ModificarCampos(UserCreationForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField(label='Correo')
    password = forms.PasswordInput
    
    GRUPOS_CHOICES = [
        ('grupo1', 'Usuarios'),
        ('grupo2', 'Administradores'),
        ('grupo3', 'Vendedores'),
    ]
    grupo = forms.ChoiceField(label='Grupo', choices=GRUPOS_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'grupo']