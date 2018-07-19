from django.template import Template, Context
from django.http import Http404, HttpResponse
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


def subirArchivo(request):
    if request.method=='POST':
        form = FormSubirArchivo(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Pc(
                usuario=request.POST['usuario'],
                sector=request.POST['sector'],
                filename=request.POST['filename'],
                archivo = request.FILES['archivo'],
            )

            newdoc.save(form)
            return redirect("subir")
    else:
        form = FormSubirArchivo()

    return render(request, 'subirArchivo.html',{'form':form})

