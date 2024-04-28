from django.urls import path
from . import views

urlpatterns = [
    path('', views.importacao, name='importacao'),
]
    