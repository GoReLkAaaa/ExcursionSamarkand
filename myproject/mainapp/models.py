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