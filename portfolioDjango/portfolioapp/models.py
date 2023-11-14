from django.db import models
from django.utils.timezone import now

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length = 256, verbose_name='Nombre', null=False, blank=False)

class Proyecto(models.Model):
    categorias = models.ManyToManyField(Categoria, verbose_name='Categoria', related_name="proyectos")
    titulo = models.CharField(max_length = 250, verbose_name='Titulo', null=False, blank=False)
    descripcion = models.TextField(verbose_name='Descripcion', null=False, blank=False)
    year = models.IntegerField(verbose_name='Año', null=False, blank=False)
    fecha_creacion = models.DateTimeField(verbose_name='Fecha creación' , default=now)
    imagen = models.ImageField(verbose_name = 'Imagen', null=True, blank=True)

