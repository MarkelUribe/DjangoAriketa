from django.db import models

# Create your models here.
class Produktuak(models.Model):
    izena = models.CharField(max_length=255)
    prezioa = models.CharField(max_length=255)