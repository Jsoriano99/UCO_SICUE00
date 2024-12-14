from django.contrib.auth.models import User
from sicue.models import Alumno

def crear_usuarios_para_alumnos():
    """
    Crea usuarios de Django para todos los alumnos que no tengan un usuario asociado.
    """
    for alumno in Alumno.objects.all():
        # Verifica si ya existe un usuario con el email del alumno
        if not User.objects.filter(email=alumno.email).exists():
            # Crear un usuario
            user = User.objects.create_user(
                username=alumno.email.split('@')[0],  # Usa la parte del email antes del @ como username
                email=alumno.email,
                password="defaultpassword123"  # Contraseña predeterminada
            )
            print(f"Usuario creado: {user.username} para el alumno {alumno.nombre}")
        else:
            print(f"El alumno {alumno.nombre} ya tiene un usuario asociado.")
