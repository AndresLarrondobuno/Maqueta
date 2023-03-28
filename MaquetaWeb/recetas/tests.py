from django.test import TestCase

nombreReceta = "Papas Rusticas"

slug = nombreReceta.lower().replace(" ", "-")

print(slug)