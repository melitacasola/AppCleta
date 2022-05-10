from django.urls import path
from AppCleta import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('inicio', views.inicio, name="Inicio"),
    path('nosotros', views.nosotros, name="Nosotros"),
    path('rutabici', views.rutabici, name="RutaBici"),
    path('autor', views.autor, name="Autor"),
    # path('formularioRuta', views.formularioRuta, name="formularioRuta"),
    # path('formularioAutor', views.formularioAutor, name="formularioAutor"),
    path('busquedaRuta', views.busquedaRuta, name="busquedaRuta"),
    path('busquedaAutor', views.busquedaAutor, name="busquedaAutor"),
    path('buscarRuta/', views.buscarRuta),
    path('buscarAutor/', views.buscarAutor),
    path('verrutas', views.verrutas, name="verrutas"),
    path('verautores', views.verautores, name="verautores"),
    path('eliminarRuta/<ruta_nombre>/', views.eliminarRuta, name="eliminarRuta"),
    path('eliminarAutor/<autor_nombre>/', views.eliminarAutor, name="eliminarAutor"),
    path('editarRuta/<ruta_nombre>/', views.editarRuta, name="editarRuta"),
    path('editarAutor/<autor_nombre>/', views.editarAutor, name="editarAutor"),
 
    path('login',views.login_request, name='login'),
    path('registro', views.register, name='Registro'),
    path('logout', LogoutView.as_view(template_name='AppCleta/logout.html'), name='Logout'),
    path('editarperfil',views.editarPerfil,name="EditarPerfil"),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
]