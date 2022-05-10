from ast import Return
from multiprocessing import context
from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse

from AppCleta.models import Autor, RutaBici, Nosotros, Avatar
from AppCleta.forms import FormularioRuta, FormularioAutor, UserRegisterForm, UserCreationForm, UserEditForm
from django.views.generic import TemplateView

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.


class HomePageViews (TemplateView):
      template_name = 'AppCleta/index.html'


@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "AppCleta/inicio.html",{"url": avatares[0].imagen.url})


def nosotros(request):
    return render(request, "AppCleta/nosotros.html")
    
@login_required
def rutabici(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "AppCleta/rutabici.html",{"url": avatares[0].imagen.url})

@login_required
def autor(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "AppCleta/autor.html",{"url": avatares[0].imagen.url})


def rutabici(request):
    return render(request, "AppCleta/rutabici.html")


def autor(request):
    return render(request, "AppCleta/autor.html")

@login_required
def rutabici(request):
    if request.method == 'POST':
        
        miFormulario = FormularioRuta(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            rutaBici = RutaBici(nombreRuta=informacion['nombreRuta'], tipoRuta=informacion['tipoRuta'], distancia=informacion['distancia'], dificultad=informacion['dificultad'], tiempo=informacion['tiempo'], comentario=informacion['comentario'])
        
            rutaBici.save()
                
            return render(request, "AppCleta/rutabici.html")
        
    else:
        miFormulario=FormularioRuta()

    return render(request, "AppCleta/rutabici.html", {"miFormulario":miFormulario})

@login_required
def autor(request):
    if request.method == 'POST':
        miFormulario = FormularioAutor(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            autor = Autor(nombre=informacion['nombre'], edad=informacion['edad'], email=informacion['email'], localidad=informacion['localidad'], sobrevos=informacion['sobrevos'], fecha=informacion['fecha'])
            autor.save()
            
            return render(request, "AppCleta/autor.html")
    else:
        miFormulario=FormularioAutor()
    return render(request, "AppCleta/autor.html", {"miFormulario":miFormulario})

def busquedaRuta(request):
    return render(request, "AppCleta/busquedaRuta.html")
    
      
def busquedaAutor(request):
    return render(request, "AppCleta/busquedaAutor.html")


def buscarRuta(request):
   
    if request.GET["nombreRuta"]:
        
        nombreRuta = request.GET["nombreRuta"]
        
        rutaBici = RutaBici.objects.filter(nombreRuta__icontains=nombreRuta)
        
        return render(request, "AppCleta/resultadoruta.html", {"nombreRuta":nombreRuta, "rutaBici":rutaBici})


    else: 
        respuesta = "Iniciar una Busqueda"     

    return HttpResponse(respuesta)


def buscarAutor(request):
    if request.GET["nombre"]:
        
        nombre = request.GET["nombre"]
        
        autor = Autor.objects.filter(nombre__icontains=nombre)
        
        return render(request, "AppCleta/resultadoautor.html", {"nombre":nombre, "autor":autor})


    else: 
        respuesta = "Iniciar una Busqueda"     

    return HttpResponse(respuesta)


def verrutas(request):
    rutas = RutaBici.objects.all()
    
    contexto= {"rutas": rutas}
    
    return render(request, "AppCleta/verrutas.html", contexto)



def verautores(request):
    autores = Autor.objects.all()
    
    contexto= {"autores": autores}
    
    return render(request, "AppCleta/verautores.html", contexto)


def eliminarRuta(request, ruta_nombre):
    rutas = RutaBici.objects.get(nombreRuta=ruta_nombre)
    rutas.delete()
    
    rutas = RutaBici.objects.all()
    contexto={"rutas": rutas}
    
    return render(request, "AppCleta/rutabici.html", contexto)


def eliminarAutor(request, autor_nombre):
    autor = Autor.objects.get(nombre=autor_nombre)
    autor.delete()
    
    autor = Autor.objects.all()
    contexto={"autor": autor}
    
    return render(request, "AppCleta/autor.html", contexto)


def editarRuta(request, ruta_nombre): 
    
    ruta = RutaBici.objects.get(nombreRuta=ruta_nombre)
    
    if request.method == "POST":
        
        miFormulario = FormularioRuta(request.POST)

        if miFormulario.is_valid():  #va con ()

            informacion = miFormulario.cleaned_data


            ruta.nombreRuta = informacion["nombreRuta"]
            ruta.tipoRuta = informacion["tipoRuta"]
            ruta.distancia = informacion["distancia"]
            ruta.dificultad = informacion["dificultad"]
            ruta.tiempo = informacion["tiempo"]
            ruta.comentario = informacion["comentario"]


            ruta.save() #Es el que guarda en la BD

        return render(request, 'AppCleta/rutabici.html')

    else:

        miFormulario = FormularioRuta(initial={"nombreRuta":ruta.nombreRuta,"tipoRuta":ruta.tipoRuta,"distancia":ruta.distancia, "dificultad":ruta.dificultad, "tiempo":ruta.tiempo, "comentario":ruta.comentario})


    return render(request, 'AppCleta/editarRuta.html',{"miFormulario":miFormulario,"ruta_nombre":ruta_nombre})



def editarAutor(request, autor_nombre): 
    
    autor = Autor.objects.get(nombre=autor_nombre)
    
    if request.method == "POST":
        
        miFormulario = FormularioAutor(request.POST)

        if miFormulario.is_valid():  #va con ()

            informacion = miFormulario.cleaned_data


            autor.nombre = informacion['nombre']
            autor.edad = informacion['edad']
            autor.email = informacion['email']
            autor.localidad = informacion['localidad']
            autor.sobrevos = informacion['sobrevos']
            autor.fecha = informacion['fecha']


            autor.save() #Es el que guarda en la BD

            return render(request, 'AppCleta/autor.html')

    else:

        miFormulario = FormularioAutor(initial={'nombre':autor.nombre,'edad':autor.edad,'email':autor.email, 'localidad':autor.localidad, 'sobrevos':autor.sobrevos, 'fecha':autor.fecha})

    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, "AppCleta/editarAutor.html",{"miFormulario":miFormulario,"autor_nombre":autor_nombre})



#login!! 

#iniciamos el login
def login_request(request):
      #capturamos el post
    if request.method == "POST":
        
        form = AuthenticationForm(request, data = request.POST)
            
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario , password = contra)
            print(1)
            
            if user is not None:
                login(request, user)

                return render (request, "AppCleta/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                print(2)
                return render (request, "AppCleta/inicio.html", {"mensaje":"Error en los datos"})
        else:
            return render(request, "AppCleta/inicio.html", {"mensaje":"Formulario erroneo"})
      
      #al final recuperamos el form
    form = AuthenticationForm()
    print(3)
    return render(request, "AppCleta/login.html", {'form': form})
  
  

def register(request):
      
    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():
                username = form.cleaned_data['username']
                 
                form.save()

                return render(request, "AppCleta/inicio.html", {"mensaje": "usuario creado"})

    else: 
        form = UserRegisterForm()

    return render(request, "AppCleta/registro.html", {"form": form})


@login_required
def editarPerfil(request):
      #se instancia el Login; 
    usuario = request.user
      
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid: #si pasa la validación Django
                informacion = miFormulario.cleaned_data
                  
                  #datos que modificaríamos
                usuario.email = informacion['email']
                usuario.password1 = informacion['password1']
                usuario.password2 = informacion['password2']
                usuario.save()
            
                return render(request, "AppCleta/inicio.html") #vuelvo a inicio

    else:
            #creo el formulario con los datos que voy a modificar
        miFormulario = UserEditForm(initial={'email':usuario.email})
      
      #voy al HTML que me permite editar
    return render(request, "AppCleta/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
