from django.urls import path
from . import views  # Importa las vistas de tu aplicación
from .views import CustomLoginView


urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("menu-profesor/", views.menu_profesor, name="menu_profesor"),
    path("menu-estudiante/", views.menu_estudiante, name="menu_estudiante"),  # Ruta del menú para estudiantes
    path("menu-administrador/", views.menu_administrador, name="menu_administrador"),  # Ruta del menú para administradores
    path("crear-solicitud/", views.crear_solicitud, name="crear_solicitud"),  # Ruta para crear solicitud
    path("listar-solicitudes/", views.listar_solicitudes, name="listar_solicitudes"),

]
