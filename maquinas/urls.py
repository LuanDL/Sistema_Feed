from django.urls import path
from . import views

urlpatterns = [
    path('', views.maquinas, name='maquinas'),
    path('cadastromaquina/',views.cadastromaquina, name="cadastromaquina")
]
