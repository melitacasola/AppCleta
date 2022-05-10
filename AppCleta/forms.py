from email.policy import default
from django import forms
import datetime
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioRuta(forms.Form):
    nombreRuta= forms.CharField()
    tipoRuta=forms.CharField()
    distancia=forms.FloatField()
    dificultad=forms.CharField()
    tiempo=forms.TimeField()
    comentario= forms.CharField()
    
    
class FormularioAutor(forms.Form):
    nombre= forms.CharField()
    edad= forms.IntegerField()
    email= forms.EmailField()
    localidad= forms.CharField()
    sobrevos= forms.CharField()
    fecha= forms.DateField(initial=datetime.date.today)
    
class UserRegisterForm(UserCreationForm):
       
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repite la contraseña', widget=forms.PasswordInput)
   
    class Meta:
        model = User                                               
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        labels = {'username': 'nombre', 'email':'correo','last_name': 'apellido', 'first_name':'nombre'}
        help_texts= {k:"" for k in fields}
        
        

class UserEditForm(UserCreationForm): 
    
    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repita contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}
        
class AvatarFormulario(forms.Form):
        
    imagen = forms.ImageField(required=True)