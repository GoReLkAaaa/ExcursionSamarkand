from django.shortcuts import render, redirect, get_object_or_404
from .models import MainDeskriptionEn, CatalogEkskursiiEn, ModalTextEn
from django.core.mail import EmailMessage
from django.http import Http404


# Create your views here.


def index(request):
    if request.method == 'GET':
        templates = 'mainapp/phoenix_wings_en.html'
        context = {
            'maincontent_en': MainDeskriptionEn.objects.all(),
        }
        return render(request, templates, context)
    else:
        name = request.POST['name']
        phone = request.POST['phone']
        city = request.POST['city']
        ekskurs = request.POST['ekskurs']
        email = 'nikitospogorelyn@gmail.com'
        try:
            subject = f'New application for excursion'
            message = f'Hello, my name is {name} \n\n'
            message += f'My phone number {phone} \n\n'
            message += f'I want to sit down {city} \n\n'
            message += f'I choose an excursion {ekskurs} \n\n'
            mail = EmailMessage(subject=subject, body=message, to=[email])
            mail.send()
            return redirect('phoenix_wings_en')
        except ValueError:
            return redirect('error_form_requests')



def index_2(request, id):
    if request.method == 'GET':
        templates = 'mainapp/eksurs_en.html'
        name_city = MainDeskriptionEn.objects.get(id=id)
        excurs = CatalogEkskursiiEn.objects.prefetch_related('modal_texts').filter(main_en_id=id)
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
        email = 'nikitospogorelyn@gmail.com'
        try:
            subject = f'New application for excursion'
            message = f'Hello, my name is {name} \n\n'
            message += f'My phone number {phone} \n\n'
            message += f'I want to sit down {city} \n\n'
            message += f'I choose an excursion {ekskurs} \n\n'
            mail = EmailMessage(subject=subject, body=message, to=[email])
            mail.send()
            return redirect('catalog', id=id)
        except ValueError:
            return redirect('error_form_requests')



def error_404(request, exception):
    return render(request, 'mainapp/404.html', status=404)



def error_form_requests(request):
    templates = 'mainapp/error_form.html'
    return render(request, templates)