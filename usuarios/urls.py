from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.usuarios, name="usuarios"),
    path('', views.login, name='login')
]
