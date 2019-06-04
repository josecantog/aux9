from django.contrib import admin
from .models import *

class EstudianteAdmin(admin.ModelAdmin):
	list_display=('nombre','correo')
	readonly_fields = ('user', 'nombre')
	fieldsets = [
        (None, {'fields':['user', 'nombre']}),
        ('Administrativo', {'fields': ['correo','numero','grupo','apodo2']}),
    ]

# Register your models here
admin.site.register(Proyecto)
admin.site.register(Grupo)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Desafio)
admin.site.register(DesafiosEstudiantes)
admin.site.register(Ramo)


