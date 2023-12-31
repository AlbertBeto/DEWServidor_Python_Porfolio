from django.contrib.messages.views import SuccessMessageMixin
from .models import Proyecto
from django.urls import reverse_lazy

class ProyectoMixin(SuccessMessageMixin):
    model = Proyecto
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('proyecto_update', kwargs={'pk': object.id})