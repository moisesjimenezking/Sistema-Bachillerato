from django import forms
from django.urls import reverse
from .models import Profesor, Materia, Seccion, Horarios


class RegModelFormProfesor(forms.ModelForm):
	
	class Meta:
		model = Profesor
		fields = ["Nombre", "Apellido", "CI", "Email", "Titulo_Profesion", "Materias_Imparte"]
		wiget = {'Materias_Imparte':forms.Select(),}
	
	def clean_CI(self):
		CI = self.cleaned_data.get("CI")
		if len(str(CI)) < 7 or len(str(CI)) > 8:
			raise forms.ValidationError("Cedula de identidad incorrecta")
		return CI


class RegModelFormHorario(forms.ModelForm):
    class Meta:
    	model = Horarios
    	fields = ["Cod_Horario",
    	"B1_Lunes","B2_Lunes",
    	"B3_Lunes","B4_Lunes",
    	"B5_Lunes","B6_Lunes",
    	"B7_Lunes","B8_Lunes",
    	"B9_Lunes","B10_Lunes",
    	"B11_Lunes",
    	"B1_Martes","B2_Martes",
    	"B3_Martes","B4_Martes",
    	"B5_Martes","B6_Martes",
    	"B7_Martes","B8_Martes",
    	"B9_Martes","B10_Martes",
    	"B11_Martes",
    	"B1_Miercoles","B2_Miercoles",
    	"B3_Miercoles","B4_Miercoles",
    	"B5_Miercoles","B6_Miercoles",
    	"B7_Miercoles","B8_Miercoles",
    	"B9_Miercoles","B10_Miercoles",
    	"B11_Miercoles",
    	"B1_Jueves","B2_Jueves",
    	"B3_Jueves","B4_Jueves",
    	"B5_Jueves","B6_Jueves",
    	"B7_Jueves","B8_Jueves",
    	"B9_Jueves","B10_Jueves",
    	"B11_Jueves",
    	"B1_Viernes","B2_Viernes",
    	"B3_Viernes","B4_Viernes",
    	"B5_Viernes","B6_Viernes",
    	"B7_Viernes","B8_Viernes",
    	"B9_Viernes","B10_Viernes",
    	"B11_Viernes",]

class RegModelFormMateria(forms.ModelForm):
	class Meta:
		model = Materia
		fields = ["Nombre"]



class RegModelFormSeccion(forms.ModelForm):
	class Meta:
		model = Seccion
		fields = ["Nombre"]

	# def clean_char(self):
	# 	Nombre_V = self.cleaned_data.get("Nombre")
	# 	element = "?"
	# 	for x in Nombre_V:
	# 		if x == "-":
	# 			element == x
	# 			break
	# 		else:
	# 			pass
	# 	if not elemtn == "-":
	# 		raise forms.ValidationError("las secciones tiene que ser identificadas cn un guion ejemplo: 2-71")
	# 	return Nombre_V