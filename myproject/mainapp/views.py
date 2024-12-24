from django.shortcuts import render, redirect
from .models import MainDeskription
from django.core.mail import EmailMessage

# Create your views here.


def index(request):
    if request.method == 'GET':
        templates = 'mainapp/index.html'
        context = {
            'maincontent': MainDeskription.objects.all(),
        }
        return render(request, templates, context)
    else:
        name = request.POST('name')
        phone = request.POST('phone')
        city = request.POST('city')
        email = 'nikitospogorelyn@gmail.com'
        try:
            subject = f'Новое письмо от {name}'
        except ValueError:
            pass




def index_2(request):
    templates = 'mainapp/index_2.html'
    return render(request, templates)