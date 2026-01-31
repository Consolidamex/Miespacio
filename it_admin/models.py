from django.db import models

class Activo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=50, unique=True)
    fecha_compra = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=50, default='Disponible')

    def __str__(self):
        return f"{self.nombre} ({self.numero_serie})"
