from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from .forms import *
from .models import *


class RecetasController(View):

    @method_decorator(login_required(login_url="/cuentas/iniciar_sesion/"))
    def agregarReceta(self, request):
        if request.method == "POST":
            form = CrearRecetaForm(request.POST)

            if form.is_valid():
                informacion = form.cleaned_data

                nombre = informacion["nombre"]
                slug = TraductorDeStrings.nombreASlug(nombre)

                receta = form.save(commit=False)
                receta.slug = slug
                receta.usuario = request.user
                receta.save()
                return redirect("recetas:inicio")
        else:
            formulario = CrearRecetaForm()
        
        return render(request, "agregarRecetaForm.html", {"form":formulario})
    

    def buscarReceta(self, request):
        if request.method == "POST":
            formularioDeBusqueda = BuscarRecetaForm(request.POST)
            if formularioDeBusqueda.is_valid():
                
                formularioDeBusqueda = formularioDeBusqueda.cleaned_data
                atributosParaFiltrado = getAtributosParaFiltrado(formularioDeBusqueda)
                recetas = Receta.objects.filter(**atributosParaFiltrado)
            return render(request, "resultadoDeBusquedaDeReceta.html", {"form":formularioDeBusqueda, "recetas":recetas})
        else:
            formularioDeBusqueda = BuscarRecetaForm()
            return render (request, "buscarRecetaForm.html", {"form":formularioDeBusqueda})
        

    def detalleReceta(self, request, slug):
        receta = Receta.objects.get(slug=slug)
        return render(request, "detalleReceta.html", {"receta":receta})
    

    def inicio(self, request):
        return render(request, "inicio.html")



def getAtributosParaFiltrado(formulario):
    atributosParaFiltrado = dict()
    for nombreDelAtributo, valor_del_atributo in formulario.items():
        if valor_del_atributo:
            atributosParaFiltrado[nombreDelAtributo] = valor_del_atributo
    
    return atributosParaFiltrado

recetasController = RecetasController()
                

                




