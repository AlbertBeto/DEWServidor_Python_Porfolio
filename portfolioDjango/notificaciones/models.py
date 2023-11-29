from django.db import models
from portfolioapp.models import Proyecto
from django.utils.timezone import now



# Create your models here.
class NotificaProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT)
    fecha = models.DateTimeField(default=now)
    notificado = models.BooleanField(default=False)
 