from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Autor(models.Model):
    
    nombre= models.CharField(max_length=40)
    edad= models.IntegerField()
    email= models.EmailField(null=True)
    localidad=models.CharField(max_length=30)
    sobrevos= models.TextField(null=True, max_length=2000)
    fecha=models.DateField(null=True)
    
    def __str__(self):
    
        return f"Autor: {self.nombre} Edad: {self.edad} de la localidad: {self.localidad} de Cordoba - contanos sobre vos: {self.sobrevos} - Fecha de creacion {self.fecha}"

class RutaBici(models.Model):
    nombreRuta=models.CharField(max_length=30)
    tipoRuta=models.CharField(max_length=30)
    distancia=models.FloatField()
    dificultad=models.CharField(max_length=10)
    tiempo=models.IntegerField()
    comentario=models.CharField(null=True, max_length=2000)
    
    def __str__(self):
        return f"RUTA - Destino: {self.nombreRuta} Tipo de Ruta: {self.tipoRuta}  - distancia aproximada: {self.distancia} km -  dificultad: {self.dificultad}  - tiempo minutos: {self.tiempo} - Comentario sobre la ruta: {self.comentario}"
        
    
class Nosotros(models.Model):
    texto=models.CharField(max_length=5000)
    
    def __str__(self):
        return f"Nosotros: {self.texto}"
    
class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta avatares media
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)