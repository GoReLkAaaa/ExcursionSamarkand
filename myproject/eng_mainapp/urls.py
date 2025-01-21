from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='phoenix_wings_en'),
    path('catalog-en/<int:id>/', views.index_2, name='catalog_en'),
    path('400/', views.error_form_requests, name='error_form_requests'),
]

