from django.contrib import admin

# Register your models here.
from .models import Categoria, Proyecto
from notificaciones.models import NotificaProyecto

class NotificaProyectoAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('proyecto', 'fecha', 'notificado')
class CategoriaAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('nombre',)
    search_fields = ['nombre']

class ProyectoAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('titulo', 'descripcion', 'year')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(NotificaProyecto,NotificaProyectoAdmin)