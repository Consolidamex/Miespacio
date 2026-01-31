from django.db import models

class Ticket(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default="Abierto")  # Abierto, En progreso, Cerrado
    asignado_a = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.estado}"
