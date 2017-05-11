from django.db import models

from apps.adopcion.models import Persona


class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    # con Python 2 se debe usar __unicode__, esto es para devolver el 'nombre' del objeto, osino devolverá Vacuna object
    def __str__(self):
        return '{}'.format(self.nombre)


class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)