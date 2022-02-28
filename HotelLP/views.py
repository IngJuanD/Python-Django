from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import HttpRequest
from django.template import Template, context
from django.template import loader
from django.shortcuts import render
from HotelLP.forms import ClienteForm, ContactoForm, ReservaForm
from HotelLP.models import Habitacion, Plan

def inicio(request):
    return render(request,"inicio.html")

#Save the dates of form web
def reserva(request):
    data={
        'form':ReservaForm()
    }
    if request.method=='POST':
        formulario=ReservaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Sus datos han sido enviados con exito!! Su reserva se realizo..."
        else:
            data["form"]=formulario

    return render(request,"reserva.html",data)

def habitaciones(request):

    lista=Habitacion.objects.all()
    return render(request,"habitaciones.html",{'habitacion':lista})

def planes(request):
    
    lista=Plan.objects.all()
    return render(request,"planes.html",{'plan':lista})


def registro(request):

    data={
        'form':ClienteForm()
    }
    if request.method=='POST':
        formulario=ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Sus datos han sido enviados con exito!! Su usuario está activo..."
        else:
            data["form"]=formulario

    return render(request,"registro.html",data)

def contacto(request):

    data={
        'form':ContactoForm()
    }
    if request.method=='POST':
        formulario=ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Sus datos han sido enviados con exito!!"
        else:
            data["form"]=formulario

    return render(request,"contacto.html",data)


def login(request):
    return render(request,"login.html")