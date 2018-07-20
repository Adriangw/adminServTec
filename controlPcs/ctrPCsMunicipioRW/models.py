from django.db import models

class Pc(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30)
    sector = models.CharField(max_length=50)
    codigo = models.CharField(max_length=30)
    archivo = models.FileField(upload_to='documents')
