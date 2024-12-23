from django.shortcuts import render
from .models import MainDeskription

# Create your views here.


def index(request):
    templates = 'mainapp/index.html'
    context = {
        'maincontent': MainDeskription.objects.all(),
    }
    return render(request, templates, context)


def index_2(request):
    templates = 'mainapp/index_2.html'
    return render(request, templates)