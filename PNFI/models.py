from django.db import models
from django.urls import reverse

# Create your models here.
class Materia(models.Model):
    Cod_Materia = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre


class Profesor(models.Model):
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    CI = models.IntegerField(primary_key=True) 
    Email = models.EmailField()
    Titulo_Profesion =models.CharField(max_length=20)
    Materias_Imparte = models.ForeignKey('Materia', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.Email


class Seccion(models.Model):
    Cod_Seccion = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.Nombre


class Horarios(models.Model):
    Horaio_id = models.AutoField(primary_key=True)
    Cod_Horario = models.ForeignKey('Seccion', on_delete=models.CASCADE, related_name= 'Cod_Horario')
    #inicio Lunes
    B1_Lunes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B1_Lunes', blank=True, null=True)
    B2_Lunes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B2_Lunes', blank=True, null=True)
    B3_Lunes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B3_Lunes', blank=True, null=True)
    B4_Lunes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B4_Lunes', blank=True, null=True)
    B5_Lunes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B5_Lunes', blank=True, null=True)
    B6_Lunes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B6_Lunes', blank=True, null=True)
    B7_Lunes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B7_Lunes', blank=True, null=True)
    B8_Lunes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B8_Lunes', blank=True, null=True)
    B9_Lunes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B9_Lunes', blank=True, null=True)
    B10_Lunes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B10_Lunes', blank=True, null=True)
    B11_Lunes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B11_Lunes', blank=True, null=True)
    #Fin Lunes
    #inicio Martes
    B1_Martes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B1_Martes', blank=True, null=True)
    B2_Martes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B2_Martes', blank=True, null=True)
    B3_Martes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B3_Martes', blank=True, null=True)
    B4_Martes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B4_Martes', blank=True, null=True)
    B5_Martes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B5_Martes', blank=True, null=True)
    B6_Martes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B6_Martes', blank=True, null=True)
    B7_Martes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B7_Martes', blank=True, null=True)
    B8_Martes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B8_Martes', blank=True, null=True)
    B9_Martes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B9_Martes', blank=True, null=True)
    B10_Martes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B10_Martes', blank=True, null=True)
    B11_Martes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B11_Martes', blank=True, null=True)
    #Fin Martes
    #inicio Miercoles
    B1_Miercoles =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B1_Miercoles', blank=True, null=True)
    B2_Miercoles =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B2_Miercoles', blank=True, null=True)
    B3_Miercoles =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B3_Miercoles', blank=True, null=True)
    B4_Miercoles =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B4_Miercoles', blank=True, null=True)
    B5_Miercoles =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B5_Miercoles', blank=True, null=True)
    B6_Miercoles =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B6_Miercoles', blank=True, null=True)
    B7_Miercoles =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B7_Miercoles', blank=True, null=True)
    B8_Miercoles =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B8_Miercoles', blank=True, null=True)
    B9_Miercoles =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B9_Miercoles', blank=True, null=True)
    B10_Miercoles =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B10_Miercoles', blank=True, null=True)
    B11_Miercoles =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B11_Miercoles', blank=True, null=True)
    #Fin Miercoles
    #inicio jueves
    B1_Jueves =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B1_Jueves', blank=True, null=True)
    B2_Jueves =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B2_Jueves', blank=True, null=True)
    B3_Jueves =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B3_Jueves', blank=True, null=True)
    B4_Jueves =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B4_Jueves', blank=True, null=True)
    B5_Jueves =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B5_Jueves', blank=True, null=True)
    B6_Jueves =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B6_Jueves', blank=True, null=True)
    B7_Jueves =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B7_Jueves', blank=True, null=True)
    B8_Jueves =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B8_Jueves', blank=True, null=True)
    B9_Jueves =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B9_Jueves', blank=True, null=True)
    B10_Jueves =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B10_Jueves', blank=True, null=True)
    B11_Jueves =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B11_Jueves', blank=True, null=True)
    #Fin jueves
    #inicio Viernes
    B1_Viernes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B1_Viernes', blank=True, null=True)
    B2_Viernes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B2_Viernes', blank=True, null=True)
    B3_Viernes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B3_Viernes', blank=True, null=True)
    B4_Viernes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B4_Viernes', blank=True, null=True)
    B5_Viernes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B5_Viernes', blank=True, null=True)
    B6_Viernes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B6_Viernes', blank=True, null=True)
    B7_Viernes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B7_Viernes', blank=True, null=True)
    B8_Viernes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B8_Viernes', blank=True, null=True)
    B9_Viernes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B9_Viernes', blank=True, null=True)
    B10_Viernes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B10_Viernes', blank=True, null=True)
    B11_Viernes =  models.ForeignKey('Materia', on_delete=models.CASCADE, related_name='B11_Viernes', blank=True, null=True)
    #Fin Viernes

    def __str__(self):
        return "Creado"