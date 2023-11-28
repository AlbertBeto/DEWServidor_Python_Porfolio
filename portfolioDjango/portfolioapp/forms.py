from django import forms
from .models import Proyecto
from django.utils import timezone
from django.core.exceptions import ValidationError

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion', 'fecha_creacion', 'year', 'categorias', 'imagen']
        #No funciona
    def clean_fecha_creacion(self):
        fecha_creacion = self.cleaned_data['fecha_creacion']
        if fecha_creacion < timezone.now():
            raise ValidationError("La fecha/hora del proyecto no puede ser anterior a la actual.")
        return fecha_creacion