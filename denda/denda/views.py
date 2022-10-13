from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Create your views here.
def index(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render({}, request))
