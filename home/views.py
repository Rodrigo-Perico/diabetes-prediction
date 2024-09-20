from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.core.validators import RegexValidator


def home(request):
    # Exibe a página inicial index.html
    return render(request, 'index.html')


validate_name = RegexValidator(r'^[a-zA-Z0-9_]+$', 'O nome deve conter apenas letras, números e underscores.')

def Cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        # Verificações básicas
        if not nome or not senha:
            messages.error(request, "Nome e senha são obrigatórios.")
            return render(request, 'Cadastro.html')

        try:
            validate_name(nome)  # Valida o nome
        except ValidationError:
            messages.error(request, "Nome inválido. Apenas letras, números e underscores são permitidos.")
            return render(request, 'Cadastro.html')

        hashed_password = make_password(senha)

        user = User(nome=nome, senha=hashed_password)
        user.save()
        
        return redirect('login')  # Nome da URL para redirecionar
    else:
        return render(request, 'Cadastro.html')

def Login(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        # Tenta encontrar o usuário no banco de dados
        try:
            user = User.objects.get(nome=nome)
        except User.DoesNotExist:
            messages.error(request, "Usuário não encontrado")
            return render(request, 'Login.html')
        # Verifica se a senha fornecida corresponde à hash armazenada
        if check_password(senha, user.senha):
            return render(request,'Painel.html')
        else:
            messages.error(request, "Senha incorreta!")
            return render(request,'Login.html')
    else:
        # Exibe a página de login Login.html
        return render(request, 'Login.html')

        
    
    
 