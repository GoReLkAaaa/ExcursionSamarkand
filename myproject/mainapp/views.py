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
        name = request.POST['name']
        phone = request.POST['phone']
        city = request.POST['city']
        email = 'nikitospogorelyn@gmail.com'
        try:
            subject = f'Новая заявка на экскурсию'
            message = f'Здравствуйте меня зовут {name} \n\n'
            message += f'Мой номер телефона {phone} \n\n'
            message += f'Я хочу поседить {city} \n\n'
            mail = EmailMessage(subject=subject, body=message, to=[email])
            mail.send()
            return redirect('index')
        except ValueError:
            return redirect('index')




def index_2(request):
    templates = 'mainapp/index_2.html'
    return render(request, templates)



def error_404(request, exception):
    return render(request, 'mainapp/404.html')