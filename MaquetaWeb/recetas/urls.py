from .views import *
from django.urls import re_path


app_name = 'recetas'

urlpatterns = [
    re_path(r'^$', recetasController.inicio, name='inicio'),
    re_path(r'^agregar_receta$', recetasController.agregarReceta, name='agregarReceta'),
    re_path(r'^buscar_receta$', recetasController.buscarReceta, name='buscarReceta'),
    re_path(r'^(?P<slug>[\w-]+)/$', recetasController.detalleReceta, name='detalle'),

]