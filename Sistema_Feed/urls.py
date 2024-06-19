from django.contrib import admin
from django.urls import path, include
from home.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('maquinas/', include('maquinas.urls')),
    path('locais/', include('locais.urls')),
    path('importacao/', include('importacao.urls')),
    path('ajuda/', include('ajuda.urls')),
    path('relatorios/',include('relatorios.urls'))
]
