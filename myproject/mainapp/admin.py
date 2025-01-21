from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import MainDeskription, CatalogEkskursii, ModalText

# Register your models here.

class ModalTextAdmin(SummernoteModelAdmin):
    summernote_fields = (
                         'name_place',
                         'take_with_you',
                        )


admin.site.register(MainDeskription)
admin.site.register(CatalogEkskursii)
admin.site.register(ModalText, ModalTextAdmin   )