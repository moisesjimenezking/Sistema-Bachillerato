"""System_Control_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from PNFI.views import Home, RegistroProfesor, RegistroMateria, RegistroSeccion, Profesores_P, Materias_P, Secciones_P, list_profesores, list_materias, list_secciones, ProfesoresUpdate, ProfesoresDelete, MateriaDelete, MateriaUpdate, RegistroHorario, HorarioDetailView, list_horarios, HorarioDelete, HorarioUpdate, SeccionDelete, SeccionUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='Home'),
    path('RegistroProfesor', RegistroProfesor, name='RegistroProfesor'),
    path('RegistroHorario', RegistroHorario, name='RegistroHorario'),
    path('RegistroSeccion', RegistroSeccion, name='RegistroSeccion'),
    path('RegistroMateria', RegistroMateria, name='RegistroMateria'),
    path('Profesores_P', Profesores_P, name='Profesores_P'),
    path('Materias_P', Materias_P, name='Materias_P'),
    path('Secciones_P', Secciones_P, name='Secciones_P'),
    path('list_profesores', list_profesores.as_view(), name='list_profesores'),
    path('list_materias', list_materias.as_view(), name='list_materias'),
    path('list_secciones', list_secciones.as_view(), name='list_secciones'),
    path('list_horarios', list_horarios.as_view(), name='list_horarios'),
    url(r'HorarioDetailView/(?P<pk>\d+)/$', HorarioDetailView.as_view(), name='HorarioDetailView'),
    url(r'ProfesoresUpdate/(?P<pk>\d+)/$', ProfesoresUpdate.as_view(), name='ProfesoresUpdate'),
    url(r'ProfesoresDelete/(?P<pk>\d+)/$', ProfesoresDelete.as_view(), name='ProfesoresDelete'),
    url(r'MateriaUpdate/(?P<pk>\d+)/$', MateriaUpdate.as_view(), name='MateriaUpdate'),
    url(r'MateriaDelete/(?P<pk>\d+)/$', MateriaDelete.as_view(), name='MateriaDelete'),
    url(r'HorarioDelete/(?P<pk>\d+)/$', HorarioDelete.as_view(), name='HorarioDelete'),
    url(r'HorarioUpdate/(?P<pk>\d+)/$', HorarioUpdate.as_view(), name='HorarioUpdate'),
    url(r'SeccionDelete/(?P<pk>\d+)/$', SeccionDelete.as_view(), name='SeccionDelete'),
    url(r'SeccionUpdate/(?P<pk>\d+)/$', SeccionUpdate.as_view(), name='SeccionUpdate'),


]
