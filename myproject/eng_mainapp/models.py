from django.db import models

# Create your models here.


class MainDeskriptionEn(models.Model):
    name_en = models.CharField(max_length=100,
                verbose_name='Название города на английском')
    description_en = models.TextField(max_length=1000, blank=True, null=True,
                verbose_name='Описание города на английском')
    image_city_en = models.ImageField(upload_to='images_en/', blank=True, null=True,
                verbose_name='Картинка города анлийской')


    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = 'Главная карточка города на английском'
        verbose_name_plural = 'Главные карточки городов на английском'


class CatalogEkskursiiEn(models.Model):
    name_excursion_en = models.CharField(max_length=100,
                verbose_name='Название экскурсии на английском')
    price_excursion_en = models.IntegerField(
                verbose_name='Цена экскурсии английской')
    image_excursion_en = models.ImageField(upload_to='image_excursion_en/',
                verbose_name='Картинка экскурсии английской')
    main_en = models.ForeignKey(MainDeskriptionEn, on_delete=models.CASCADE, related_name='main_en',
                verbose_name='К какому городу относится англ')

    def __str__(self):
        return self.name_excursion_en


    class Meta:
        verbose_name = 'Экскурсия города англ'
        verbose_name_plural = 'Экскурсии городов англ'



class ModalTextEn(models.Model):
    how_long_en = models.CharField(max_length=100,
                verbose_name='Сколько длится поездка англ')
    name_place_en = models.TextField(max_length=5500,
                verbose_name='Название локаций и места на выбор с указанием времени англ')
    time_to_departure_en = models.CharField(max_length=100,
                verbose_name='Во сколько выезд англ')
    take_with_you_en = models.TextField(max_length=1500,
                verbose_name='Что взять с собой англ')
    how_many_day_and_night_en = models.CharField(max_length=100,
                verbose_name='За сколько дней и ночей англ')
    how_many_people_en = models.IntegerField(
                verbose_name='Стоимость за сколько человек англ')
    price_russian_en = models.IntegerField(
                verbose_name='Цена за русскую поездку англ')
    price_english_en = models.IntegerField(
                verbose_name='Цена за английскую поездку англ')
    what_is_not_included_in_price_en = models.CharField(max_length=200,
                verbose_name='Что не входит в стоимость')
    modal_ekskurs_name_en = models.ForeignKey(CatalogEkskursiiEn, on_delete=models.CASCADE, related_name='modal_texts',
                verbose_name='К какой экскурсии отосится англ')

    def __str__(self):
        return self.modal_ekskurs_name_en.name_excursion_en


    class Meta:
        verbose_name = 'Модальные окна англ'
        verbose_name_plural = 'Модальное окно англ'