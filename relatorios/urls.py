from django.urls import path
from . import views

urlpatterns = [
    path('relatoriousuarios/', views.relatoriousuarios, name="relatoriousuarios"),
    path('relatoriomaquinas/', views.relatoriomaquinas, name="relatoriomaquinas"),
    path('relatoriolocais/', views.relatoriolocais, name="relatoriolocais"),
]