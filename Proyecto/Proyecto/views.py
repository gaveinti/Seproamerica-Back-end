from contextvars import Context
from pipes import Template
from pydoc import doc
from re import template
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
import datetime

def inicioSesion(request): # Primera vista
    #Se abre el doc de la plantilla
    plantillaExterna = open("./plantillas/inicio_Sesion.html")
    #Se carga el doc en una variable de tipo plantilla
    template = Template(plantillaExterna.read())
    #Se cierra el doc externo abierto
    plantillaExterna.close()

    #Se crea un contexto
    contexto = Context()
    #Se renderiza la plantilla
    documento = template.render(contexto)


    return HttpResponse(documento)
    #return render(request, 'inicio_Sesion.html')