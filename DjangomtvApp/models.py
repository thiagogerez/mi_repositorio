from django.db import models

class Lista(models.Model):
    nombre = models.CharField(max_length=10)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    nacimiento = models.IntegerField()
