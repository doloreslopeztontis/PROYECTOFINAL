"""here URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from heredjapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('materias/', views.materia_list),
    path('materias/<int:id>', views.materia_detail),
    path('materias/materianew', views.materia_new),
    path('profesores/', views.profesor_list),
    path('profesores/<int:dni>', views.profesor_detail),
    path('profesores/<int:dni>/materias', views.profesor_materias),
    path('profesores/profesornew', views.profesor_new),
    path('profesores/<int:dni>/materianew', views.profesor_new_materia),
]
