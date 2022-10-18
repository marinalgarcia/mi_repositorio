from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    numero_documento = models.IntegerField()
    codigo_postal = models.IntegerField()

def __str__(self):
    return f"{self.nombre}, {self.numero_documento}, {self.id}"
