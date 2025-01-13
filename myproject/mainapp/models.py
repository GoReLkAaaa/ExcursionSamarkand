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


class ModalText(models.Model):
    how_long = models.CharField(max_length=100, verbose_name='Сколько длится поездка')
    name_place = models.TextField(max_length=1500, verbose_name='Название локаций и места на выбор с указанием времени')
    time_to_departure = models.CharField(max_length=100, verbose_name='Во сколько выезд')
    take_with_you = models.TextField(max_length=500, verbose_name='Что взять с собой')
    how_many_day_and_night = models.CharField(max_length=100, verbose_name='За сколько дней и ночей')
    how_many_people = models.IntegerField(verbose_name='Стоимость за сколько человек')
    price_russian = models.IntegerField(verbose_name='Цена за русскую поездку')
    price_english = models.IntegerField(verbose_name='Цена за английскую поездку')
    what_is_not_included_in_price = models.CharField(max_length=200, verbose_name='Что не входит в стоимость')
    modal_ekskurs_name = models.ForeignKey(CatalogEkskursii, on_delete=models.CASCADE, related_name='modal_texts', verbose_name='К какой экскурсии отосится')

    def __str__(self):
        return self.name_place


    class Meta:
        verbose_name = 'Модальные окна'
        verbose_name_plural = 'Модальное окно'