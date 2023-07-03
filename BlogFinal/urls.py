from django.urls import path
from BlogFinal import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.presentacion, name="Presentacion"),
    path('inicio', views.inicio, name="Inicio"),
    path('register', views.register, name="Register"),
    path('login', views.login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name='BlogFinal/inicio.html'), name='Logout'),
    path('aboutme', views.aboutme, name="Aboutme"),
    path('añadirPublicaciones', views.añadirPublicaciones, name="addPost"),
    path('editarPerfil', views.editarPerfil, name="Perfil"),
    path('post/<int:pk>', views.verPost, name="verPost"),
    path('editar/<int:pk>', views.publicacionUpdate.as_view(), name='Edit'),
    path('borrar/<int:pk>', views.publicacionDelete.as_view(), name='Delete'),
    path('misPosts', views.misPost, name="misPost"),
    path('buscar/', views.buscar),
]
