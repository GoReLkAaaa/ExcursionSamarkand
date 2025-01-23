from django.contrib import admin
from .models import MainDeskriptionEn, CatalogEkskursiiEn, ModalTextEn
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import User, Group
from django_summernote.models import Attachment

# Register your models here.

class ModalTextAdmin(SummernoteModelAdmin):
    summernote_fields = (
                         'name_place_en',
                         'take_with_you_en',
                        )


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(Attachment)

admin.site.register(MainDeskriptionEn)
admin.site.register(CatalogEkskursiiEn)
admin.site.register(ModalTextEn, ModalTextAdmin)