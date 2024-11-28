from django.shortcuts import render

# Create your views here.


def index(request):
    templates = 'mainapp/index.html'
    return render(request, templates)