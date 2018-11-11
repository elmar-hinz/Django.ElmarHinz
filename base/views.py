from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.template import TemplateDoesNotExist


def index(request):
    return render(request, 'base/index.html')

def site(request, name):
    try:
        return render(request, 'base/' + name)
    except TemplateDoesNotExist:
        raise Http404("Page does not exist")

