from django.shortcuts import render
from django.http import HttpResponse
from usuarios.models import Perfil
import re

def validar_email(email):
    return re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email)

def usuarios(request):
    if request.method == "GET":
        usuario_list = Perfil.objects.all()
        return render(request, 'CadUsuarios.html', {'usuarios': usuario_list})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        # ... outros campos ...

        # Consultar se o email já foi cadastrado
        usuarios_query = Perfil.objects.filter(email=email)
        if usuarios_query.exists():
            return render(request, 'CadUsuarios.html', {
                'error_message': 'Email já cadastrado.',
                # ... outros campos para preencher o formulário novamente ...
            })

        # Consultar se o email é valido
        if not validar_email(email):
            return render(request, 'CadUsuarios.html', {
                'error_message': 'Email inválido.',
                # ... outros campos para preencher o formulário novamente ...
            })

        # Se passar pelas validações, criar o novo usuário
        novo_usuario = Perfil(
            nome=nome,
            email=email,
            # ... outros campos ...
        )
        novo_usuario.save()
        return HttpResponse('Usuário criado com sucesso!')

    # Se não for GET nem POST, retorna um erro 405
    return HttpResponse('Método não permitido', status=405)
