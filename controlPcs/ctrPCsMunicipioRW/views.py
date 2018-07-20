from django.template import Template, Context
from django.http import Http404, HttpResponse
from django.http import FileResponse
from django.template.loader import get_template
from django.shortcuts import render, redirect
from ctrPCsMunicipioRW.forms import FormSubirArchivo
from ctrPCsMunicipioRW.models import Pc
import datetime

HTML = """
    <html>
        <body>
            <h1>HOLA MUNDO!</h1>
        </body>
    </html>
"""
def hola(request):
    return HttpResponse(HTML)

def inicio(request):
    return render(request, 'inicio.html')

 
def bajarSpeccy(request): 
     #datos_imagen = open("/home/adrian/djangoProjects/adminServTec/controlPcs/speccy/imagen.jpeg", "rb").read() 
     #return HttpResponse(datos_imagen, mimetype="imagen/jpeg") 
     response = FileResponse(open('/home/adrian/djangoProjects/adminServTec/controlPcs/speccy/Speccy.exe', 'rb'))
     response['Content-Type'] = 'application/octet-stream'
     return response

def subirArchivo(request):
    
    if request.method=='POST':
        form = FormSubirArchivo(request.POST, request.FILES)
        if form.is_valid():
            newPC = Pc(
                usuario = request.POST['usuario'],
                sector = request.POST['sector'],
                archivo = request.FILES['archivo'],
            )
            ultimo_id = Pc.objects.latest('id')#Se obtiene el ultimo objeto cargado en la base de datos.
            newPC.codigo = "st-" + str(ultimo_id.id + 1)#Se genera un codigo automaticamente para el equipo en base al id
            newPC.save(form)
            return redirect("subir")
    else:
        form = FormSubirArchivo()

    return render(request, 'subirArchivo.html',{'form':form})

