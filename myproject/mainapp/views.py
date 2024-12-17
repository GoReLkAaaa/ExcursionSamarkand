from django.shortcuts import render

# Create your views here.


def index(request):
    templates = 'mainapp/index.html'
    return render(request, templates)


def index_2(request):
    templates = 'mainapp/index_2.html'
    return render(request, templates)