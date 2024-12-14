from django.contrib import admin
from .models import Alumno, Profesor, Administrador

# Registrar el modelo Alumno
@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email', 'matricula', 'carrera')

# Registrar el modelo Profesor
@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email', 'departamento', 'especialidad')

# Registrar el modelo Administrador
@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email', 'rol')
