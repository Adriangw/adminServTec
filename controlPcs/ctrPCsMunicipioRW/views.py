from django.template import Template, Context
from django.http import Http404, HttpResponse
from django.http import FileResponse
from django.template.loader import get_template
from django.shortcuts import render, redirect
from ctrPCsMunicipioRW.forms import FormSubirArchivo
from ctrPCsMunicipioRW.models import Pc
import os
from xml.dom import minidom
import datetime
from ctrPCsMunicipioRW.leerxml import obtenerDataPC


def inicio(request):
    return render(request, 'inicio.html')

 
def bajarSpeccy(request): 
     #datos_imagen = open("/home/adrian/djangoProjects/adminServTec/controlPcs/speccy/imagen.jpeg", "rb").read() 
     #return HttpResponse(datos_imagen, mimetype="imagen/jpeg") 
     my_data = open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/speccy/Speccy.exe', 'rb')
     response = HttpResponse(my_data, content_type='application/vnd.microsoft.portable-executable')
     response['Content-Disposition'] = 'attachment; filename="speccy.exe"'
     return response

def subirArchivo(request):
    
    if request.method=='POST':
        form = FormSubirArchivo(request.POST, request.FILES)
        if form.is_valid():
            datosPc={}
            newPC = Pc(
                usuario = request.POST['usuario'],
                sector = request.POST['sector'],
                archivo = request.FILES['archivo'],
            )
            ultimo_id = Pc.objects.latest('id')#Se obtiene el ultimo objeto cargado en la base de datos.
            newPC.codigo = "st-" + str(ultimo_id.id + 1)#Se genera un codigo automaticamente para el equipo en base al id
            newPC.save(form)
            newPc.codigo
            datosPc=obtenerDataPC(newPc.codigo)

            print("--->",datosPc['CPU'])

            return redirect("subir")
    else:
        form = FormSubirArchivo()

    return render(request, 'subirArchivo.html',{'form':form})

