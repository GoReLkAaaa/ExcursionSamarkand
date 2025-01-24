from django.shortcuts import render, redirect
from .models import MainDeskription, CatalogEkskursii
from django.core.mail import EmailMessage
from django.http import Http404

# Create your views here.


def index(request):
    if request.method == 'GET':
        templates = 'mainapp/phoenix_wings.html'
        context = {
            'maincontent': MainDeskription.objects.all(),
        }
        return render(request, templates, context)
    else:
        name = request.POST['name']
        phone = request.POST['phone']
        city = request.POST['city']
        ekskurs = request.POST['ekskurs']
        email = 'bysiyavush@gmail.com'
        try:
            subject = f'Новая заявка на экскурсию'
            message = f'Здравствуйте меня зовут {name} \n\n'
            message += f'Мой номер телефона {phone} \n\n'
            message += f'Я хочу поседить {city} \n\n'
            message += f'Я выбираю экскурсию {ekskurs} \n\n'
            mail = EmailMessage(subject=subject, body=message, to=[email])
            mail.send()
            return redirect('phoenix_wings')
        except ValueError:
            return redirect('page_not_found')



def index_2(request, id):
    if request.method == 'GET':
        templates = 'mainapp/index_2.html'
        name_city = MainDeskription.objects.get(id=id)
        excurs = CatalogEkskursii.objects.prefetch_related('modal_texts').filter(main_id=id)
        context = {
            'name_city': name_city,
            'excurs': excurs,
        }
        if not excurs.exists():
            raise Http404('Ничего не найдено')
        return render(request, templates, context)
    else:
        name = request.POST['name']
        phone = request.POST['phone']
        city = request.POST['city']
        ekskurs = request.POST['ekskurs']
        email = 'bysiyavush@gmail.com'
        try:
            subject = f'Новая заявка на экскурсию'
            message = f'Здравствуйте меня зовут {name} \n\n'
            message += f'Мой номер телефона {phone} \n\n'
            message += f'Я хочу поседить {city} \n\n'
            message += f'Я выбираю экскурсию {ekskurs} \n\n'
            mail = EmailMessage(subject=subject, body=message, to=[email])
            mail.send()
            return redirect('catalog', id=id)
        except ValueError:
            return redirect('page_not_found')



def error_404(request, exception):
    return render(request, 'mainapp/404.html', status=404)



def error_form_requests(request):
    templates = 'mainapp/error_form.html'
    return render(request, templates)