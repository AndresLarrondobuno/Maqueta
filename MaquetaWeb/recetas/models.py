from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=50) #Ingrediente con Foreign Key
    preparacion = models.TextField()
    fechaYHorario = models.DateTimeField()
    slug = models.CharField(max_length=50)


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



