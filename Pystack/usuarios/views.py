from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')
        if not senha == confirmar_senha:
            messages.add_message(request,constants.ERROR, 'As senhas nao sao iguais')
            return redirect('/usuarios/cadastro')

        if len(senha) < 8:
            messages.add_message(request,constants.ERROR, 'Sua senha deve ter 8 ou mais digitos')
            return redirect('/usuarios/cadastro')
        try:
            user = User.objects.create_user(
                username=username,
                password=senha,
                email=email,
                first_name=primeiro_nome,
                last_name=ultimo_nome
                
        
        )
            messages.add_message(request,constants.SUCCESS,'Usuario salvo com sucesso')
        except:
            messages.add_message(request,constants.ERROR,'Erro do sistema')
            return redirect('/usuarios/cadastro')
        return redirect('/usuarios/cadastro')
def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        try:
            user = authenticate(username=username, password=senha)
            if user:
                login(request,user)
                return redirect('/')
            if user.check_password(senha):
                messages.add_message(request,constants.SUCCESS,'Login efetuado com sucesso')
                return redirect('/usuarios/login')
            else:
                messages.add_message(request,constants.ERROR,'Senha incorreta')
                return redirect('/usuarios/login')
        except:
            messages.add_message(request,constants.ERROR,'Usuario ou senha incorreto')
            return redirect('/usuarios/login')