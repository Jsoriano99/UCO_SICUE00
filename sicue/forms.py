from django import forms
from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['universidad_origen', 'universidad_destino', 'fecha_inicio', 'fecha_fin', 'motivo']

