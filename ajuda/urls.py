from django.urls import path
from . import views

urlpatterns = [
    path('', views.ajuda, name='ajuda'),
]
