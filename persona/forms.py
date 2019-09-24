from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models as m
from django.contrib import auth


class PersonaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }
            
    class Meta:
        model = m.Persona
        fields = (
            'rol',
            'edad'
        )

    def save(self,commit=True):
        persona = super(PersonaForm,self).save(commit=False)
        if commit:
            persona.save()
            return persona

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
            }
            self.fields['username'].widget.attrs = {
                'placeholder':'correo@email.com',
                'class': 'form-control', 
                'required' : 'true',
                'oninvalid':'AlertaCorreo()'
            }
            self.fields['username'].label = 'Correo-Nombre de usuario'

    class Meta:
        model = User
        fields=(
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        )

    def save(self,commit=True):
        user= super(UserForm,self).save(commit=False)
        if commit:
            user.save()
            return user