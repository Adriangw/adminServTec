from django import forms

class FormSubirArchivo(forms.Form):
    usuario = forms.CharField(max_length=30, widget=forms.TextInput(

        attrs={
            "class":"form-control form_control-lg",
            
            "placeholder":"Ingrese el Usuario Actual de la Computadora.",
            "id":"IDusuario",
        }
    ))
    sector = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Ingrese el sector lugar de trabajo.",
            "id" : "IDsector",

        }

    ))

    fecha = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Ingrese la fecha actual.",
            "id" : "IDfecha",
        }

    ))

    """
    filename = forms.CharField(label="Nombre Archivo",required=False, max_length=50, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Ingrese el nombre de archivo.",
            "id" : "IDfilename",
        }

    ))
    """
    
    archivo = forms.FileField(widget=forms.FileInput(
        attrs={
            "class" : "form-control-file",
            "id" : "IDinputFile",
        }

    ))
