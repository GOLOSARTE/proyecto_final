from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Publicacion(models.Model):
    autor = models.ForeignKey(User, on_delete= models.CASCADE, default=1)
    titulo = models.CharField(max_length=25)
    fecha = models.DateField(auto_now_add= True)
    imagen = models.ImageField(upload_to='publicaciones/', default= 'imagen')
    descripcion = models.CharField(max_length=400)
    provincia = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=20)
    indicaciones = models.CharField(max_length=200)



class Comentario(models.Model):
    comentario = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add= True)
    autor = models.ForeignKey(User, on_delete= models.CASCADE, default=1)
    publi = models.CharField(max_length=25)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
