from django.shortcuts import render
from django.http import HttpResponse

def relatoriousuarios(request):
    return render(request, 'RelatorioUsu.html')

def relatoriomaquinas(request):
    return render(request, 'RelatorioMaq.html')

def relatoriolocais(request):
    return render(request, 'RelatorioLoc.html')
