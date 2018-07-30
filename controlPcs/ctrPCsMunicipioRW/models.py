from django.db import models

class Pc(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30)
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
