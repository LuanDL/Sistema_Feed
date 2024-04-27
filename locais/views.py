from django.shortcuts import render
from django.http import HttpResponse
from .models import Locais

def locais(request):
        if request.method == "GET":
                return render(request,'CadLocais.html')
        elif request.method == "POST":
                usuario = request.POST.get('usuarios')
                local = request.POST.get('locais')
                maquina = request.POST.get('maquinas')

                maquina = Locais(
                        usuarios = usuario,
                        locais = locais,
                        maquinas = maquina,
                )

                local.save()

                print(usuario, local, maquina)

                return render(request,'CadLocais.html')