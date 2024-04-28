from django.shortcuts import render
from django.http import HttpResponse

def ajuda(request):
    return render(request,'ajuda.html')