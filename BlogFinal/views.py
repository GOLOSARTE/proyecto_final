from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from BlogFinal.forms import UserRegisterForm, UserEditForm, publicacionesFormulario, comentariosFormulario
from BlogFinal.models import Publicacion,Comentario,Avatar
from django.contrib.auth.models import User
from django.shortcuts import redirect


def inicio(request):

      posts = Publicacion.objects.all()

      contexto = {"posts" : posts}
      return render(request, "BlogFinal/inicio.html", contexto)



def register(request):
      if request.method == 'POST':

            form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return redirect('/login')

      else:
            form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"BlogFinal/registro.html" ,  {"form":form})


def login_request(request):
      

      if request.method == 'POST':
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():  # Si pasó la validación de Django

                  usuario = form.cleaned_data.get('username')
                  contrasenia = form.cleaned_data.get('password')

                  user = authenticate(username= usuario, password=contrasenia)

                  if user is not None:
                        login(request, user)

                        return redirect('/inicio')
            
                  else:

                        form = AuthenticationForm()   
                        return render(request, "BlogFinal/login.html", {"mensaje":"Datos incorrectos"}, {"form": form})
         


            else:

                  form = AuthenticationForm()   
                  return render(request, "BlogFinal/login.html"  , {"form": form, "mensaje" : "Datos incorrectos"})
                  


      form = AuthenticationForm()

      return render(request, "BlogFinal/login.html", {"form": form})


@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()

            return redirect('/inicio')

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "BlogFinal/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})




def aboutme(request):
      return render(request, "BlogFinal/aboutme.html")

from datetime import datetime
@login_required
def añadirPublicaciones(request):
      if request.method == 'POST':
            miFormulario = publicacionesFormulario(request.POST, request.FILES)


            if miFormulario.is_valid():

                  informacion = miFormulario.cleaned_data
                  fechanow = datetime.now()
                  usuario = (User.objects.get(username = request.user)) 
                  
                  post = Publicacion(

                  fecha = fechanow,
                  autor = usuario,
                  titulo = informacion["titulo"],
                  imagen = informacion["imagen"],
                  descripcion = informacion["descripcion"],
                  provincia = informacion["provincia"] ,
                  ciudad = informacion["ciudad"], 
                  indicaciones = informacion["indicaciones"]
                  
                  )
                  
                  post.save()
                  return redirect('/inicio')

      
      else: 

            miFormulario = publicacionesFormulario()
      
      return render(request, "BlogFinal/añadirPublicaciones.html",  {"miFormulario": miFormulario})


def buscar(request):

      if request.GET["titulo"]:
            titulo = request.GET["titulo"]
            publicaciones = Publicacion.objects.filter(titulo__icontains = titulo)

            return render(request, "BlogFinal/inicio.html", {"publicaciones" : publicaciones, "titulo" : titulo})

      
      else: 

	      return  "No enviaste datos"

@login_required
def misPost(request):
      
      
      posts = Publicacion.objects.all()
      usuario = (User.objects.get(username = request.user)) 
      autor = usuario

      contexto = {"posts" : posts, "usuario" : usuario, "autor" : autor}
      return render(request, "BlogFinal/misPublicaciones.html", contexto)





def presentacion(request):
      return render(request, "BlogFinal/presentacion.html")



from django.views.generic.edit import CreateView,DeleteView,UpdateView     

@login_required
def verPost(request, pk):
    post = Publicacion.objects.get(id=pk)
    usuario = (User.objects.get(username = request.user)) 
    comentarios = Comentario.objects.all()
    miFormulario = comentariosFormulario()

    if request.method == 'POST':
        miFormulario = comentariosFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            fechanow = datetime.now()
            comment = Comentario(
                fecha = fechanow,
                autor = usuario,
                comentario = informacion["comentario"],
                publi = post.titulo
                
                  
            )
            comment.save()
            return redirect('/BlogFinal/post/' + str(post.id))

    contexto = {'post': post, 'usuario' : usuario ,'miFormulario' : miFormulario, "comentarios" : comentarios}

    return render(request, "BlogFinal/verPost.html", contexto)



#update
class publicacionUpdate(UpdateView):
      model = Publicacion
      success_url = "/BlogFinal/inicio"
      fields = ['titulo', 'descripcion', 'provincia', 'ciudad', 'indicaciones', 'imagen']     


###############################


#delete
class publicacionDelete(DeleteView):
      model = Publicacion
      success_url = "/BlogFinal/inicio"



#############################################################*
###################################################################







###############################
