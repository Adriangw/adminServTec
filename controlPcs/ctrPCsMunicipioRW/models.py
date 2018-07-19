from django.db import models

class Pc(models.Model):
    usuario = models.CharField(max_length=30,blank=True)
    sector = models.CharField(max_length=50,blank=True)
    filename = models.CharField(max_length=100,blank=True)
    archivo = models.FileField(upload_to='documents',blank=True)
