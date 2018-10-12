from django.db import models

# Create your models here.
class Region(models.Model):
	Id_Region = models.PositiveSmallIntegerField()
	Descripcion = models.CharField(max_length=20)

class Ciudad(models.Model):
	Region = models.ForeignKey(Region, null=False,blank=False, on_delete = models.CASCADE)
	Id_Ciudad = models.PositiveSmallIntegerField()
	Descripcion = models.CharField(max_length=20)
	
class Tipo_Vivienda(models.Model):
	Id_Tipo_Vivienda = models.PositiveSmallIntegerField()
	Descripcion = models.CharField(max_length=20)
	
class Vivienda(models.Model):
	Tipo_Vivienda = models.ForeignKey(Tipo_Vivienda, null=False,blank=False, on_delete = models.CASCADE)
	Id_Vivienda = models.PositiveSmallIntegerField()
	Descripcion = models.CharField(max_length=20)
	
class Usuario(models.Model):
	Vivienda = models.ForeignKey(Vivienda, null=False,blank=False, on_delete = models.CASCADE)
	Correo = models.CharField(max_length=40)
	Run = models.CharField(max_length=10)
	Nombre = models.CharField(max_length=100)
	Apellido = models.CharField(max_length=100)
	Fecha_Nacimineto = models.DateField()
	Fono =models.PositiveSmallIntegerField()
	
	

	
	



	
