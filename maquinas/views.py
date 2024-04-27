from django.shortcuts import render
from django.http import HttpResponse
from .models import Maquinas

def maquinas(request):
        if request.method == "GET":
                return render(request,'cadmaquinas.html')
        elif request.method == "POST":
                nome = request.POST.get('Maqnome')
                codigo = request.POST.get('Maqcod')
                status = request.POST.get('MaqStatus') == 'True'

                maquina = Maquinas(
                        nome = nome,
                        codigo = codigo,
                        status = status,
                )

                maquina.save()

                print(nome, codigo, status)

                return render(request,'cadmaquinas.html')