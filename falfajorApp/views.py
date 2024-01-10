from django.shortcuts import render, HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from falfajorApp.models import Alfajor, Clientes, Pedidos
from falfajorApp.forms import AlfajoresFormulario, ClientesFormulario


# Create your views here.
def alfajor(request):

      alfajor =  Alfajor(nombre="La Dominga", camada="12345")
      alfajor.save()
      documentoDeTexto = f"--->Curso: {alfajor.nombre}   Camada: {alfajor.camada}"


      return HttpResponse(documentoDeTexto)

def inicio(request):

      return render(request, "falfajorApp/inicio.html")

def pedidos(request):

      return render(request, "falfajorApp/pedidos.html")



def alfajores(request):

      if request.method == 'POST':

            miForm = AlfajoresFormulario(request.POST) 

            print(miForm)

            if miForm.is_valid:   

                  informacion = miForm.cleaned_data

                  curso = Alfajor (nombre=informacion['alfajor'], codigo_alfajor=informacion['codigo_alfajor']) 

                  curso.save()

                  return render(request, "falfajorApp/inicio.html") 

      else: 

            miForm= AlfajoresFormulario()

      return render(request, "falfajorApp/alfajores.html", {"miForm":miForm})

def clientes(request):

      if request.method == 'POST':

            miForm2= ClientesFormulario(request.POST) 

            print(miForm2)

            if miForm2.is_valid:   

                  data = miForm2.cleaned_data

                  profesor = Clientes (nombre=data['nombre'], apellido=data['apellido'],
                   email=data['email'], telefono=data['telefono']) 

                  profesor.save()

                  return render(request, "falfajorApp/inicio.html") 

      else: 

            miForm2= ClientesFormulario() #Formulario vacio para construir el html

      return render(request, "falfajorApp/clientes.html", {"miForm2":miForm2})

def buscar(request):

      if  request.GET["codigo_alfajor"]:

	      #respuesta = f"Estoy buscando la codigo_alfajor nro: {request.GET['codigo_alfajor'] }" 
            codigo_alfajor = request.GET['codigo_alfajor'] 
            alfajor = Alfajor.objects.filter(codigo_alfajor__icontains=codigo_alfajor)

            return render(request, "falfajorApp/inicio.html", {"alfajor":alfajor, "codigo_alfajor":codigo_alfajor})

      else: 
        respuesta = "enviar datos por favor"

        return HttpResponse(respuesta)