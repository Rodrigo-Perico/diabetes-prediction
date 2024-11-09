from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import User, Cadastro
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.core.validators import RegexValidator
import pickle  


def load_model():
    with open('./modelos/diabetes_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def predict_diabetes(features):
    model = load_model()
    prediction = model.predict(features)
    return prediction[0]

validate_crm = RegexValidator(r'^[a-zA-Z0-9_]+$', 'O CRM deve conter apenas letras, números e underscores.')

def home(request):
    return render(request, 'index.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        CRM = request.POST.get('CRM')
        senha = request.POST.get('senha')

        if not CRM or not senha:
            messages.error(request, "CRM e senha são obrigatórios.")
            return render(request, 'Cadastro.html')

        try:
            validate_crm(CRM)
        except ValidationError:
            messages.error(request, "CRM inválido.")
            return render(request, 'Cadastro.html')

        if User.objects.filter(CRM=CRM).exists():
            messages.error(request, "Este CRM já está registrado.")
            return render(request, 'Cadastro.html')

        hashed_password = make_password(senha)
        user = User(CRM=CRM, senha=hashed_password)
        user.save()
        
        messages.success(request, "Usuário cadastrado com sucesso!")
        return redirect('login')

    return render(request, 'Cadastro.html')

def Login(request):
    if request.method == 'POST':
        CRM = request.POST.get('CRM')
        senha = request.POST.get('senha')

        try:
            user = User.objects.get(CRM=CRM)
        except User.DoesNotExist:
            messages.error(request, "CRM ou senha incorreta!")
            return render(request, 'Login.html')

        if check_password(senha, user.senha):
            request.session['user_crm'] = CRM
            return redirect('consulta')
        else:
            messages.error(request, "CRM ou senha incorreta!")
            return render(request, 'Login.html')
    return render(request, 'Login.html')

def Consulta(request):
    if request.method == 'POST':
        CRM = request.session.get('user_crm')
        if not CRM:
            messages.error(request, "Usuário não autenticado.")
            return redirect('login')
        
        try:
            user = User.objects.get(CRM=CRM)
            cadastro = Cadastro(
                user=user,
                pressao_alta=request.POST.get('pressao_alta'),
                colesterol_alto=request.POST.get('colesterol_alto'),
                checagem_colesterol=request.POST.get('checagem_colesterol'),
                imc=float(request.POST.get('imc')),
                fumante=request.POST.get('fumante'),
                avc=request.POST.get('avc'),
                doencas_cardiacas=request.POST.get('doencas_cardiacas'),
                atividades_fisicas=request.POST.get('atividades_fisicas'),
                consome_frutas=request.POST.get('consome_frutas'),
                consome_vegetais=request.POST.get('consome_vegetais'),
                alto_consumo_alcool=request.POST.get('alto_consumo_alcool'),
                possui_convenio=request.POST.get('possui_convenio'),
                evitou_consultas=request.POST.get('evitou_consultas'),
                saude_geral=request.POST.get('saude_geral'),
                saude_mental=request.POST.get('saude_mental'),
                saude_fisica=request.POST.get('saude_fisica'),
                dificuldade_andar=request.POST.get('dificuldade_andar'),
                genero=request.POST.get('genero'),
                idade=request.POST.get('idade'),
                escolaridade=request.POST.get('escolaridade'),
                renda=request.POST.get('renda'),
            )
            
            cadastro.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('home')
        except Exception as e:
            messages.error(request, f"Erro ao salvar o cadastro: {e}")
            return render(request, 'Consulta.html')
    
    return render(request, 'Consulta.html')
