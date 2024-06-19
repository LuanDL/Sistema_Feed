from django.shortcuts import render
from django.http import HttpResponse
from .forms import formulariomaquina

def maquinas(request):
        form = formulariomaquina()
        return render(request,'cadmaquinas.html', {'form': form})

def cadastromaquina(request):
       form = formulariomaquina(request.POST)
       if form.is_valid():
                form.save()
                nome = form.data['nome']
                codigo = form.data['codigo']
                status = form.data['status']
                return HttpResponse('Salvo com sucesso')
       return  HttpResponse('Erro ao cadastrar')