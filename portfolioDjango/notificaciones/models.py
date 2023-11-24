from django.db import models
from portfolioapp.models import Proyecto
from django.utils.timezone import now

# Create your models here.
class NotificaProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT)
    fecha = models.DateTimeField(default=now)
    notificado = models.BooleanField(default=False)
    
    #Escrito pero no confirmado 3.6.1
    def form_valid(self, form):
        if form.instance.fecha_creacion < timezone.now():
            messages.error(self.request, "La fecha/hora del proyecto no puede ser anterior a la actual.")
            return super(ProyectoCreateView, self).form_invalid(form)
        else:
            proyecto = form.save()
            NotificaProyecto.objects.create(proyecto=proyecto)
            return super(ProyectoCreateView, self).form_valid(form)