
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from BlogFinal.models import Publicacion, Comentario, Avatar






class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput )
    password2 = forms.CharField(label = "Repetir contraseña", widget=forms.PasswordInput )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):

    # Obligatorios
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')   
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)



    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2' ]


class publicacionesFormulario(forms.Form):
    titulo = forms.CharField(max_length=25)
    descripcion = forms.CharField(max_length=400, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}))
    provincia = forms.CharField(max_length=15)
    ciudad = forms.CharField(max_length=20)
    indicaciones = forms.CharField(max_length=200)
    imagen = forms.ImageField()


class comentariosFormulario(forms.Form):
    comentario = forms.CharField(max_length=200, label="" ,widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}))
