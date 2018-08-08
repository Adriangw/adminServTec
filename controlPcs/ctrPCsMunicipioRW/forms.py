from django import forms
from ctrPCsMunicipioRW.models import SECTOR

class FormSubirArchivo(forms.Form):
    usuario = forms.CharField(max_length=30, widget=forms.TextInput(

        attrs={
            "class":"form-control form_control-lg",
            
            "placeholder":"Ingrese el Usuario Actual de la Computadora.",
            "id":"IDusuario",
        }
    ))

    secretaria = forms.ChoiceField(choices = SECTOR, label="Secretaria",initial=1,widget=forms.Select(attrs={"class":"form-control",}),required=True)

  
    
    sector = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            "class": "form-control pure-form",
            "onsubmit" : "$('#hero-demo').blur();return false;",
            "placeholder": "Ingrese el sector lugar de trabajo.",
            "id" : "hero-demo",
            "name":"q",
        }
    ))	

    fecha = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Ingrese la fecha actual.",
            "id" : "IDfecha",
        }

    ))

    archivo = forms.FileField(widget=forms.FileInput(
        attrs={
            "class" : "form-control-file",
            "id" : "IDinputFile",
        }

    ))
