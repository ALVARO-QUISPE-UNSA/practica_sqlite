"""
URL configuration for peliculas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from consultas_pweb2 import views as consultas_pweb2_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('peliculas/', consultas_pweb2_view.lista_peliculas, name='Lista de peliculas'),
    path('', consultas_pweb2_view.vista_index, name="Página principal"),
    path('consultas', consultas_pweb2_view.get_datos, name='Obtener tablas'),
]
