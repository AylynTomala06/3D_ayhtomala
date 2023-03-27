from django.shortcuts import render
from.models import libros, ulector, alquiler
from .forms import LibrosForm
# Create your views here.
def inicio(request):
    libro= libros.objects.all()
    data={
        'libros': libro
    }
    return render(request,'libreriaapp/inicio.html',data)


def basedef(request):
    return render(request, 'libreriaapp/base.html', {})

def ulectorf(request):
    lector = ulector.objects.all()
    data = {
        'ulector': lector
    }
    return render(request,'libreriaapp/lectores.html',data)

def alquilerf(request):
    alquileres = alquiler.objects.all()
    data = {
        'alquiler': alquileres
    }
    return render(request, 'libreriaapp/alquiler.html',data)

#OPCIONES AGREGAR, EDITAR y ELIMINAR
def agregarlibro(request):
    data={
        'form': LibrosForm()
    }
    return render(request,'libreriaapp/agregarlibro.html',data )

'''
def eliminar(request,id):
    libros=get_object_or_404(libros, where id=id)
    libros.delete()
    return redirect(to='inicio')
'''