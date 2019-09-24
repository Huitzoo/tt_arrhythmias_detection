from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def main(request):
    return render(request,'main.html',)

"""
@login_required(redirect_field_name='login')
def princial(request):
    return render(request,'dashboard.html')


def login_authenticate(request):
    username = request.POST.get("username",None)
    user = authenticate(username=username, password=request.POST.get("password",None))
    if user is not None:
        login(request, user)
        messages.add_message(request, messages.SUCCESS, 'Bienvenido, '+username)
        return redirect('principal')
        # A backend authenticated the credentials
    else:
        messages.add_message(request, messages.ERROR, 'El correo electrónico o el password no son correctos.')
        return redirect('main')
        # No backend authenticated the credentials

@login_required(redirect_field_name='login')
def logout_authenticate(request):
    logout(request)
    return redirect('main')
"""

def arritmias(request):
    return render(request,"arritmias.html")
