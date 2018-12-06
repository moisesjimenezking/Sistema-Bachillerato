from django.contrib import admin
from .models import Profesor, Seccion, Materia, Horarios
from .forms import RegModelFormProfesor, RegModelFormMateria, RegModelFormSeccion, RegModelFormHorario
# Register your models here.

class AdminProfesor(admin.ModelAdmin):
    list_display = ["Nombre", "Apellido", "CI", "Email", "Titulo_Profesion"]
    form = RegModelFormProfesor
    search_fields = ["Nombre", "CI", "Titulo_Profesion"]

class AdminMateria(admin.ModelAdmin):
    list_display = ["Cod_Materia","Nombre"]
    form = RegModelFormMateria
    search_fields = ["Nombre"]

class AdminSeccion(admin.ModelAdmin):
    list_display = ["Nombre"]
    form = RegModelFormSeccion
    search_fields = ["Nombre"]


class AdminHorarios(admin.ModelAdmin):
	list_display = ["Cod_Horario"]
	form = RegModelFormHorario
	search_fields = ["Cod_Horario"]

admin.site.register(Horarios, AdminHorarios)
admin.site.register(Profesor, AdminProfesor)
admin.site.register(Seccion, AdminSeccion)
admin.site.register(Materia, AdminMateria)