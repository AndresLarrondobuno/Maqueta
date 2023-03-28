from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import *
from .models import *

# Create your views here.
class UsuariosController(View):

    
    def registrarUsuarioView(self, request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():        
                user = form.save()
                login(request, user)
                #logear usuario
                return redirect('recetas:inicio')    
        else:
            form = UserCreationForm()
        return render(request, 'registrarUsuarioForm.html', {"form":form})


    def iniciarSesionView(self, request):
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('recetas:inicio')
        else:
            form = AuthenticationForm()
        return render(request, 'iniciarSesionForm.html', {"form":form})
    

    def cerrarSesionView(self, request):
        if request.method == "POST":
            logout(request)
            return redirect('recetas:inicio')


usuariosController = UsuariosController()