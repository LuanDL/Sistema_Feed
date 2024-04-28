from django.shortcuts import render
from django.http import HttpResponse

def importacao(request):
    return render(request,'importacao.html')