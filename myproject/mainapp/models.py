from django.db import models

# Create your models here.


class MainDeskription(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название города')
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Описание города')
    image_city = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Картинка города')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Главная карточка города'
        verbose_name_plural = 'Главные карточки городов'


class CatalogEkskursii(models.Model):
    name_excursion = models.CharField(max_length=100, verbose_name='Название экскурсии')
    price_excursion = models.IntegerField(verbose_name='Цена экскурсии')
    image_excursion = models.ImageField(upload_to='image_excursion/', verbose_name='Картинка экскурсии')
    main = models.ForeignKey(MainDeskription, on_delete=models.CASCADE, related_name='main', verbose_name='К какому городу относится')

    def __str__(self):
        return self.name_excursion


    class Meta:
        verbose_name = 'Экскурсия города'
        verbose_name_plural = 'Экскурсии городов'
