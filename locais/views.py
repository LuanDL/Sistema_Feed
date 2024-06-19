from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormularioLocais

def locais(request):
    form = FormularioLocais()
    return render(request, 'cadLocais.html', {'form':form})

def cadastrolocal(request):
    form = FormularioLocais(request.POST)
    if form.is_valid():
        form.save()
        usuario = form.data['usuario']
        local = form.data['local']
        maquina = form.data['maquina']
        return HttpResponse('Salvo com sucesso')
    return HttpResponse('Erro ao cadastrar')