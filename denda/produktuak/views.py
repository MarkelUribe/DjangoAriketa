from django.template import loader
from django.shortcuts import render
from .models import *
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    produktuak = Produktuak.objects.all()
    template = loader.get_template('index.html')
    context = {
        'produktuak': produktuak,
    }
    return HttpResponse(template.render(context, request))