from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    bezeroak = Bezero.objects.all()
    template = loader.get_template('my.html')
    context = {
        'bezeroak': bezeroak,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addbezero(request):
    x = request.POST['izena']
    y = request.POST['abizena']
    z = request.POST['adina']
    bezero = Bezero(izena=x, abizena=y, adina=z)
    bezero.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  bezero = Bezero.objects.get(id=id)
  bezero.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  bezero = Bezero.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'bezero': bezero,
  }
  return HttpResponse(template.render(context, request))

def updatebezero(request, id):
  izena = request.POST['izena']
  abizena = request.POST['abizena']
  adina = request.POST['adina']
  bezero = Bezero.objects.get(id=id)
  bezero.izena = izena
  bezero.abizena = abizena
  bezero.adina = adina
  bezero.save()
  return HttpResponseRedirect(reverse('index'))