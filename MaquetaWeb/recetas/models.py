from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=50) #Ingrediente con Foreign Key
    preparacion = models.TextField()
    fechaYHorario = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, default=None, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre
    

    def snippet(self):
        return self.preparacion[:50] + "..."
    

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre


class TraductorDeStrings:
    def nombreASlug(nombre):
        slug = nombre.lower().replace(" ", "-")
        return slug



