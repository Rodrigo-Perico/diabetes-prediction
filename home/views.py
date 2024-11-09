from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import User, Cadastro
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.core.validators import RegexValidator
import pickle

# Função para carregar o modelo de diabetes
def load_model():
    with open('./modelos/diabetes_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Função para fazer a previsão de diabetes
def predict_diabetes(features):
    model = load_model()  # Carrega o modelo uma vez
    prediction = model.predict(features)
    return prediction[0]  # Retorna a previsão (por exemplo, 0 ou 1)

# Exibe a página inicial
def home(request):
    return render(request, 'index.html')

# Validador de CRM
validate_crm = RegexValidator(r'^[a-zA-Z0-9_]+$', 'O CRM deve conter apenas letras, números e underscores.')

def cadastrar_usuario(request):
    if request.method == 'POST':
        CRM = request.POST.get('CRM')
        senha = request.POST.get('senha')

        # Verificações básicas
        if not CRM or not senha:
            messages.error(request, "CRM e senha são obrigatórios.")
            return render(request, 'Cadastro.html')

        try:
            validate_crm(CRM)  # Valida o CRM
        except ValidationError:
            messages.error(request, "CRM inválido.")
            return render(request, 'Cadastro.html')

        hashed_password = make_password(senha)

        # Criação do usuário
        user = User(CRM=CRM, senha=hashed_password)
        user.save()
        
        messages.success(request, "Usuário cadastrado com sucesso!")
        return redirect('login')  # Redireciona para a página de login
    else:
        return render(request, 'Cadastro.html')

def Login(request):
    if request.method == 'POST':
        CRM = request.POST.get('CRM')
        senha = request.POST.get('senha')

        # Tenta encontrar o usuário no banco de dados
        try:
            user = User.objects.get(CRM=CRM)
        except User.DoesNotExist:
            messages.error(request, "Usuário não encontrado.")
            return render(request, 'Login.html')

        # Verifica a senha
        if check_password(senha, user.senha):
            return render(request, 'Consulta.html')  # Redireciona para a consulta
        else:
            messages.error(request, "Senha incorreta!")
            return render(request, 'Login.html')
    else:
        return render(request, 'Login.html')

def Consulta(request):
    if request.method == 'POST':
        # Obtenha os dados do formulário
        CRM = request.POST.get('CRM')  # Supondo que o CRM também seja enviado no formulário
        pressao_alta = request.POST.get('pressao_alta')
        colesterol_alto = request.POST.get('colesterol_alto')
        checagem_colesterol = request.POST.get('checagem_colesterol')
        imc = request.POST.get('imc')
        fumante = request.POST.get('fumante')
        avc = request.POST.get('avc')
        doencas_cardiacas = request.POST.get('doencas_cardiacas')
        atividades_fisicas = request.POST.get('atividades_fisicas')
        consome_frutas = request.POST.get('consome_frutas')
        consome_vegetais = request.POST.get('consome_vegetais')
        alto_consumo_alcool = request.POST.get('alto_consumo_alcool')
        possui_convenio = request.POST.get('possui_convenio')
        evitou_consultas = request.POST.get('evitou_consultas')
        saude_geral = request.POST.get('saude_geral')
        saude_mental = request.POST.get('saude_mental')
        saude_fisica = request.POST.get('saude_fisica')
        dificuldade_andar = request.POST.get('dificuldade_andar')
        genero = request.POST.get('genero')
        idade = request.POST.get('idade')
        escolaridade = request.POST.get('escolaridade')
        renda = request.POST.get('renda')

        # Verificações básicas
        if not pressao_alta or not colesterol_alto or not imc:
            messages.error(request, "Pressão alta, colesterol alto e IMC são obrigatórios.")
            return render(request, 'Consulta.html')

        # Validação de IMC
        try:
            imc = float(imc)  # Converte o IMC para float
            if imc < 0:
                raise ValueError("IMC deve ser um número positivo.")
        except ValueError:
            messages.error(request, "IMC inválido.")
            return render(request, 'Consulta.html')

        # Associando o usuário ao cadastro
        try:
            user = User.objects.get(CRM=CRM)  # Encontrando o usuário pelo CRM
        except User.DoesNotExist:
            messages.error(request, "Usuário não encontrado.")
            return render(request, 'Consulta.html')

        # Criação e salvamento do objeto Cadastro
        cadastro = Cadastro(
            user=user,  # Associa o cadastro ao usuário
            pressao_alta=pressao_alta,
            colesterol_alto=colesterol_alto,
            checagem_colesterol=checagem_colesterol,
            imc=imc,
            fumante=fumante,
            avc=avc,
            doencas_cardiacas=doencas_cardiacas,
            atividades_fisicas=atividades_fisicas,
            consome_frutas=consome_frutas,
            consome_vegetais=consome_vegetais,
            alto_consumo_alcool=alto_consumo_alcool,
            possui_convenio=possui_convenio,
            evitou_consultas=evitou_consultas,
            saude_geral=saude_geral,
            saude_mental=saude_mental,
            saude_fisica=saude_fisica,
            dificuldade_andar=dificuldade_andar,
            genero=genero,
            idade=idade,
            escolaridade=escolaridade,
            renda=renda
        )
        
        try:
            cadastro.save()  # Salva o cadastro
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('home')
        except Exception as e:
            messages.error(request, f"Erro ao salvar o cadastro: {e}")
            return render(request, 'Consulta.html')
    
    return render(request, 'Consulta.html')
