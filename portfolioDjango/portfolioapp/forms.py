from django import forms
from .models import Proyecto
from django.utils import timezone
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field, ButtonHolder, Submit, HTML, Row

class ProyectoForm(forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super(ProyectoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False # No incluir <form></form>
        
        self.helper.layout = Layout(
            Div(
            Field('titulo'),
            Field('descripcion'),
        ),
        HTML('<hr>'),
        Div(
            Div(Field('fecha_creacion'), css_class="col-6"),
            Div(Field('year'), css_class="col-6"),
            css_class="row"
        ),
        HTML('<hr>'),
        Div(
            Field('categorias', css_class="mb-3"),
            Field('imagen'),
            css_class="mb-5"
        ),
        )
    
    def clean_fecha_creacion(self):
        fecha_creacion = self.cleaned_data['fecha_creacion']
        if fecha_creacion < timezone.now():
            raise ValidationError("La fecha/hora del proyecto no puede ser anterior a la actual.")
        return fecha_creacion
    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion', 'fecha_creacion', 'year', 'categorias', 'imagen']
        #No funciona