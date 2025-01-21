from django.contrib import admin
from .models import MainDeskriptionEn, CatalogEkskursiiEn, ModalTextEn
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class ModalTextAdmin(SummernoteModelAdmin):
    summernote_fields = (
                         'name_place_en',
                         'take_with_you_en',
                        )


admin.site.register(MainDeskriptionEn)
admin.site.register(CatalogEkskursiiEn)
admin.site.register(ModalTextEn, ModalTextAdmin)