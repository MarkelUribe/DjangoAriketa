from time import timezone
from django.db import models
from django.utils import timezone

# Create your models here.
class Bezero(models.Model):
    izena = models.CharField(max_length=30)
    abizena = models.CharField(max_length=30)
    adina = models.CharField(max_length=30)
    erosketa = models.DateTimeField(default=timezone.now)
    
    def bought(self):
        self.purchase_date = timezone.now()
        
    def __str__(self) -> str:
        return u'%s' % self.izena