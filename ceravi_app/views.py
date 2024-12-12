from datetime import datetime
import random, time
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import login as django_login

#importações dos modelos (classes) necessários para o UC login
from ceravi_app.models import Usuario

#a seguir são definidas as funções que possuem lógica dos controladores no padrão MVC

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        # Verifica se o email e a senha são válidos
        usuario = consultarUsuario(email, senha)

        if usuario:
            # Redireciona para a página inicial do sistema
            return redirect("pagina_inicial") 
        else:
            # Usuário não está cadastrado ou a senha está incorreta
            return render(request, "ceravi/login.html", {"error": "E-mail ou senha inválidos."})

    # Exibe a página de login para requisições GET
    return render(request, "ceravi/login.html")
    

def consultarUsuario(email, senha):
    return Usuario.logar(email, senha) #chama a função logar do model, que retorna o objeto ou false

def cadastro(request):
    return render(request, "ceravi/cadastro.html")

def esqueceu_senha(request):
    return render(request, "ceravi/esqueceu_senha.html")

def pagina_inicial(request):
    return render(request, "ceravi/pagina_inicial.html")
