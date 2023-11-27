from django.shortcuts import render # Para FBV
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView # Para CBV
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .mixins import ProyectoMixin
from django.contrib import messages
from django.db import transaction
from django.utils import timezone
from notificaciones.models import NotificaProyecto
# Create your views here.

from .models import Proyecto
def home_view(request):
    proyectos = Proyecto.objects.all()
    context={'proyectos': proyectos}
    return render(request, 'portfolio/home.html', context)

class HomeView(TemplateView):
    template_name = 'portfolio/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        cat_id = kwargs.get('cat_id')
        context['proyectos'] = Proyecto.objects.filter(categorias__id=cat_id) if cat_id else Proyecto.objects.all()
        
        return context

def proyecto_view(request,pk):
    proyecto = get_object_or_404(Proyecto,pk=pk)
    context = {'proyecto': proyecto}
    return render(request,'portfolio/proyecto.html',context)

class ProyectoView(TemplateView):
    template_name = 'portfolio/proyecto.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ProyectoView, self).get_context_data(**kwargs)
        context['proyecto'] = get_object_or_404(Proyecto,id=kwargs['pk'])
        return context  

def contacto_view(request):
    context = {'full_name':'Albert Pérez Baleyto'}
    return render(request,'portfolio/contacto.html', context)

class ContactoView(TemplateView):
    template_name = 'portfolio/contacto.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ContactoView, self).get_context_data(**kwargs)
        context['full_name'] = 'Albert Pérez Baleyto'
        return context 

class ProyectoCreateView(ProyectoMixin, CreateView):
    success_message = "Proyecto creado exitosamente"

    def form_valid(self, form):
        if form.instance.fecha_creacion < timezone.now():
            messages.error(self.request, "La fecha/hora del proyecto no puede ser anterior a la actual.")
            return super(ProyectoCreateView, self).form_invalid(form)
        else:
            proyecto = form.save()
            NotificaProyecto.objects.create(proyecto=proyecto)
            return super(ProyectoCreateView, self).form_valid(form)
    

class ProyectoUpdateView(ProyectoMixin, UpdateView):
    success_message = "Proyecto creado exitosamente"

   

class ProyectoDeleteView(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('home')
