"""
URL configuration for portfolioDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from portfolioapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('home_fbv', views.home_view, name='home_fbv'),
    path('', views.HomeView.as_view(), name='home'),
    path('<int:cat_id>/', views.HomeView.as_view(), name='home'),
    #path('proyecto/<int:pk>/', views.proyecto_view, name='proyecto'),
    path('proyecto/<int:pk>/', views.ProyectoView.as_view(), name='proyecto'),
    #path('contacto/', views.contacto_view, name='contacto'),
    path('contacto/', views.ContactoView.as_view(), name='contacto'),
    path('proyecto_create/', views.ProyectoCreateView.as_view(), name='proyecto_create'),
    path('proyecto_update/<int:pk>/', views.ProyectoUpdateView.as_view(), name='proyecto_update'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    