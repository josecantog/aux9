from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proyecto(models.Model):
	descripcion=models.CharField(max_length=512)
	cliente=models.CharField(max_length=30)
	fecha_limite=models.DateField()

class Grupo(models.Model):
	nombre=models.CharField(max_length=30)
	proyecto= models.OneToOneField(Proyecto, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

class Estudiante(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

	nombre=models.CharField(max_length=30)
	correo=models.EmailField(max_length=256)
	numero=models.IntegerField(null=True)
	grupo=models.ForeignKey(Grupo, on_delete=models.CASCADE)
	apodo2=models.CharField(max_length=30)

class Desafio(models.Model):
	titulo=models.CharField(max_length=30)
	descripcion=models.CharField(max_length=512)
	fecha=models.DateField()

class DesafiosEstudiantes(models.Model):
	estudiante=models.ForeignKey(Estudiante,on_delete=models.CASCADE)
	desafio=models.ForeignKey(Desafio, on_delete=models.CASCADE)
	fueEntregado=models.BooleanField(default=False)

class Ramo(models.Model):
	nombre_ramo=models.CharField(max_length=30)
	departamento=models.CharField(max_length=512)
	uds=models.IntegerField()