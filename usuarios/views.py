from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def usuarios(request):
    if request.method == "GET":
        return render(request, 'CadUsuarios.html')
    else:
        username = request.POST.get('username')
        email= request.POST.get('email')
        senha = request.POST.get('senha')
        cep = request.POST.get('cep')
        endereco = request.POST.get('endereco')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        telefone = request.POST.get('telefone')
        celular = request.POST.get('celular')
        grupoacesso = request.POST.get('grupoacesso')
        observacoes = request.POST.get('observacoes')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse username')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

    return HttpResponse ('Usuário cadastrado com sucesso')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return HttpResponse('autenticado')
        else:
            return HttpResponse('Email ou senha invalidos')