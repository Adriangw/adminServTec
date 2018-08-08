from django.db import models

SECTOR = (
        (1, "Seleccione La Secretaria que Corresponde"),
        (2, "SECRETARIA DE HACIENDA"),
        (3, "SECRETARIA DE GOBIERNO"),
        (4, "SECRETARIA DE FAMILIA"),
        (5, "SECRETARIA DE CULTURA"),
        (6, "SECRETARIA DE PLANIFICACION")
    )

class Sector(models.Model):
    FILTROS = ["sector__icontains"]
    sector = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % (self.sector)


class Pc(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30)
    secretaria = models.PositiveIntegerField(choices=SECTOR)
    sector = models.CharField(max_length=50)
    codigo = models.CharField(max_length=30)
    archivo = models.FileField(upload_to='documents')
    so = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    madre = models.CharField(max_length=100)
    graf = models.CharField(max_length=100)
    disk = models.CharField(max_length=100)
    optic = models.CharField(max_length=100)
    audio = models.CharField(max_length=100)
    mac = models.TextField()
    name = models.TextField()
