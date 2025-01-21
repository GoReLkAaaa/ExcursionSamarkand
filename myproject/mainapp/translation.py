from modeltranslation.translator import TranslationOptions, translator
from .models import MainDeskription, CatalogEkskursii, ModalText


class MainDeskriptionTranslationOptions(TranslationOptions):
    class Meta:
        fields = '__all__'


class CatalogEkskursiiTranslationOptions(TranslationOptions):
    class Meta:
        fields = '__all__'


class ModalTextTranslationOptions(TranslationOptions):
    class Meta:
        fields = '__all__'


translator.register(MainDeskription, MainDeskriptionTranslationOptions)
translator.register(CatalogEkskursii, CatalogEkskursiiTranslationOptions)
translator.register(ModalText, ModalTextTranslationOptions)