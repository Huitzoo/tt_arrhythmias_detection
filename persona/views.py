from django.shortcuts import render
from . import forms

# Create your views here.

def registrar(request):
    if request.method == 'POST':
        return render()
    else:
        registrar_form = forms.PersonaForm()
        user_form = forms.UserForm()
        ctx = {
            "user":user_form,
            "registrar":registrar_form
        }
        
        return render(request,"registrar.html",ctx)
