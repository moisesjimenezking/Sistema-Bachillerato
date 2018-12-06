from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from .forms import  RegModelFormProfesor, RegModelFormMateria, RegModelFormSeccion, RegModelFormHorario
from .models import Materia, Profesor, Seccion, Horarios
# Create your views here

def Home(request):
    return render(request,'html/Home.html', {})


def Profesores_P(request):
	return render(request, 'html/Profesores.html', {})


def Materias_P(request):
	return render(request, 'html/Materias.html', {})


def Secciones_P(request):
	return render(request, 'html/Secciones.html', {})

class list_profesores(ListView):
    model = Profesor
    template_name = "html/list_profesores.html"
    #return render(request, 'html/list_profesores.html', {})

class list_materias(ListView):
	model = Materia
	template_name = "html/list_materias.html"
	#return render(request, 'html/list_materias.html', {})

class list_secciones(ListView):
	model = Seccion
	template_name = "html/list_secciones.html"
	#return render(request, 'html/list_secciones.html', {})


class list_horarios(ListView):
	model = Horarios
	template_name = "html/list_horarios.html"

def RegistroProfesor(request):
	form = RegModelFormProfesor(request.POST or None)
	context = {"form":form,}
	
	if form.is_valid():
		Titulo = "Profesor añadido por el Administrador"
		instance = form.save(commit = False)
		instance.save()
		context ={"Titulo":Titulo,} 
	
	return render(request, 'html/RegProfesor.html', context)


def RegistroHorario(request):
	form = RegModelFormHorario(request.POST or None)
	context = {"form":form,}

	if form.is_valid():
		Titulo = "Horario creado"
		instance = form.save(commit = False)
		instance.save()
		context = {"Titulo":Titulo,}

	return render(request, 'html/RegHorario.html', context)



def RegistroMateria(request):
	form = RegModelFormMateria(request.POST or None)
	context = {"form":form}
	
	if form.is_valid():
		Titulo = "Profesor añadido por el Administrador"
		isnstance = form.save(commit = False)
		isnstance.save()
		context = {"Titulo":Titulo,}
	
	return render(request, 'html/RegMateria.html', context)


def RegistroSeccion(request):
	form = RegModelFormSeccion(request.POST or None)
	context = {"form":form}
	
	if form.is_valid():
		Titulo = "Profesor añadido por el Administrador"
		isnstance = form.save(commit = False)
		isnstance.save()
		context = {"Titulo":Titulo,}

	return render(request, 'html/RegSeccion.html', context)

class ProfesoresUpdate(UpdateView):
	model = Profesor
	form_class = RegModelFormProfesor
	template_name = "html/ProfesoresUpdate.html"
	success_url = reverse_lazy('list_profesores')


class ProfesoresDelete(DeleteView):
	model = Profesor
	form_class = RegModelFormProfesor
	template_name = "html/ProfesoresDelete.html"
	success_url = reverse_lazy('list_profesores')

class MateriaUpdate(UpdateView):
	model = Materia
	form_class = RegModelFormMateria
	template_name = "html/MateriaUpdate.html"
	success_url = reverse_lazy('list_materias')

class HorarioUpdate(UpdateView):
	model = Horarios
	form_class = RegModelFormHorario
	template_name = "html/HorarioUpdate.html"
	success_url = reverse_lazy('list_horarios')
		
class MateriaDelete(DeleteView):
	model = Materia
	form_class = RegModelFormMateria
	template_name = "html/MateriaDelete.html"
	success_url = reverse_lazy('list_materias')


class SeccionUpdate(UpdateView):
	model = Seccion
	form_class = RegModelFormSeccion
	template_name = "html/SeccionUpdate.html"
	success_url = reverse_lazy('list_secciones')
		
class SeccionDelete(DeleteView):
	model = Seccion
	form_class = RegModelFormSeccion
	template_name = "html/SeccionDelete.html"
	success_url = reverse_lazy('list_secciones')


class HorarioDetailView(DetailView):
	model = Horarios
	form_class = RegModelFormHorario
	template_name = "html/horarios_detail.html"
	success_url = reverse_lazy('list_secciones')


class HorarioDelete(DeleteView):
	model = Horarios
	form_class = RegModelFormHorario
	template_name = "html/HorarioDelete.html"
	success_url = reverse_lazy('list_horarios')
# class ProfesoresDelete(UpdateView):
# 	model = Profesor
# 	form_class = RegModelFormProfesor
# 	template_name = "html/RegProfesor.html"

# def ProfesoresEdit(request, CI_Profesor):
# 	print(dir(Profesor))
# 	profesor = Profesor(CI=CI_Profesor)#.order_by("CI")
# 	if request.method == 'GET':
# 		form = RegModelFormProfesor(isinstance=profesor)
# 	else:
# 		form = RegModelFormProfesor(request.POST, isinstance=profesor)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('list_profesores')
# 	return render(request, 'html/list_profesores.html', {'form':form})