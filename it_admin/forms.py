from django import forms
from .models import Activo

class ActivoForm(forms.ModelForm):
    class Meta:
        model = Activo
        fields = ['nombre', 'tipo', 'numero_serie', 'fecha_compra', 'estado']
