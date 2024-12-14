import os
import django

# Configuración para usar Django fuera del shell interactivo
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sicue_project.settings')
django.setup()

from django.contrib.auth.models import User

# Listar todos los superusuarios
superusers = User.objects.filter(is_superuser=True)
if superusers.exists():
    for user in superusers:
        print(f"Superusuario: {user.username}, Email: {user.email}")
else:
    print("No hay superusuarios creados.")
