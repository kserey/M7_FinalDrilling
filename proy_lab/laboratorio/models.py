from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255, null=True, blank=True)
    pais = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255, null=True, blank=True)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


def validar_fecha_fabricacion(value):
    if value.year < 2015:
        raise ValidationError("La fecha de fabricación no puede ser anterior a 2015.")

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(validators=[validar_fecha_fabricacion])
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.laboratorio.nombre})"