from datetime import datetime
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import User, Cadastro
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.core.validators import RegexValidator
import pickle  
import pandas as pd
import sklearn


def load_model():
    # Usando barras normais
    with open('home/modelos/modelo_logistic.pkl', 'rb') as f:
        modelo = pickle.load(f)
    return modelo

def predict_diabetes(features):
    model = load_model()
    prediction = model.predict(features)
    return prediction[0]

validate_crm = RegexValidator(
    r'^\d{4,6}-[A-Za-z]{2}$', 
    'O CRM deve conter de 4 a 6 dígitos seguidos por um hífen e a sigla do estado (ex: 12345-SP).'
)

def home(request):
    return render(request, './home/index.html')

def Painel(request):
    return render(request, './home/Painel.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        CRM = request.POST.get('CRM')
        senha = request.POST.get('senha')

        if not CRM or not senha:
            messages.error(request, "CRM e senha são obrigatórios.")
            return render(request, './home/Cadastro.html')

        try:
            validate_crm(CRM)
        except ValidationError:
            messages.error(request, "CRM inválido.")
            return render(request, './home/Cadastro.html')

        if User.objects.filter(CRM=CRM).exists():
            messages.error(request, "Este CRM já está registrado.") # Enumeração de usuários, o ideal é não informar.
            return render(request, './home/Cadastro.html')

        hashed_password = make_password(senha)
        user = User(CRM=CRM, senha=hashed_password)
        user.save()
        
        return redirect('login')

    return render(request, './home/Cadastro.html')
    
def Login(request):
    if request.method == 'POST':
        CRM = request.POST.get('CRM')
        senha = request.POST.get('senha')

        try:
            user = User.objects.get(CRM=CRM)
        except User.DoesNotExist:
            messages.error(request, "CRM ou senha incorreta!")
            return render(request, './home/Login.html')

        if check_password(senha, user.senha):
            request.session['user_crm'] = CRM
            return redirect('consulta')
        else:
            messages.error(request, "CRM ou senha incorreta!")
    return render(request, './home/Login.html')

def Consulta(request):
    CRM = request.session.get('user_crm')
    if not CRM:
        messages.error(request, "Você tentou acessar a área de consulta sem estar autenticado. Por favor, faça login para continuar.")
        return redirect('login')

    if request.method == 'POST':
        CRM = request.session.get('user_crm')
        if not CRM:
            messages.error(request, "Usuário não autenticado.")
            return redirect('login')
        
        try:
            # Obtenção do usuário autenticado
            user = User.objects.get(CRM=CRM)
            
            # Extração e transformação dos dados para predição
            features = [
                int(request.POST.get('pressao_alta')),
                int(request.POST.get('colesterol_alto')),
                int(request.POST.get('checagem_colesterol')),
                int(request.POST.get('imc')),
                int(request.POST.get('fumante')),
                int(request.POST.get('avc')),
                int(request.POST.get('doencas_cardiacas')),
                int(request.POST.get('atividades_fisicas')),
                int(request.POST.get('consome_frutas')),
                int(request.POST.get('consome_vegetais')),
                int(request.POST.get('alto_consumo_alcool')),
                int(request.POST.get('possui_convenio')),
                int(request.POST.get('evitou_consultas')),
                int(request.POST.get('saude_geral')),
                int(request.POST.get('saude_mental')),
                int(request.POST.get('saude_fisica')),
                int(request.POST.get('dificuldade_andar')),
                int(request.POST.get('genero')),
                int(request.POST.get('idade')),
                int(request.POST.get('escolaridade')),
                int(request.POST.get('renda'))
            ]
            
            features = [features]
            input_df = pd.DataFrame(features, columns=['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke',
                'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
                'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth',
                'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education',
                'Income'])
            print(features)

            prediction = predict_diabetes(input_df)

            print(prediction)
        
            # Tratamento da data para garantir que esteja no formato correto


            # Salvar cadastro no banco de dados
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
                predict=int(prediction),
                cpf=request.POST.get('cpf'),
                data_predicao= request.POST.get('data_predicao')
            )
            cadastro.save()
            mensagem = ""
            # Exibir resultado da predição
            if prediction == 1:
                mensagem = 'O resultado da predição de diabetes é POSITIVA !'
                          
                return render(request, './home/Consulta.html', {'mensagem': mensagem})
            else:
                mensagem = 'O resultado da predição de diabetes é NEGATIVA !'
                return render(request, './home/Consulta.html', {'mensagem': mensagem})
        except Exception as e:
            return render(request, './home/Consulta.html')
    
    return render(request, './home/Consulta.html')
    


"""
def consulta_historico(request):
    form_type = request.POST.get()
    if request.method == 'POST':
        # Captura o valor do CPF enviado pelo formulário
        cpf_consulta = request.POST.get('cpf_consulta')

        try:
            if Cadastro.objects.filter(cpf=cpf_consulta).exists():

                cadastro = Cadastro.objects.filter(cpf=cpf_consulta).first()
                return render(request, './home/consulta_cpf.html', {'cadastro': cadastro})
        

        except Exception as e:
        # Verifica se o CPF foi enviado
            if not cpf_consulta:
                return HttpResponse("Por favor, insira o CPF.")
            
            # Verifique se o CPF tem 11 dígitos (validação básica)
            if len(cpf_consulta) != 11 or not cpf_consulta.isdigit():
                return HttpResponse("CPF inválido. Certifique-se de que ele possui 11 números.")
            
            # Aqui você pode realizar uma consulta no banco de dados ou outro processamento
            # Por exemplo:
            # paciente = Paciente.objects.filter(cpf=cpf_consulta).first()
            
            # Para fins de exemplo, consideramos que a consulta foi bem-sucedida:
            return HttpResponse(f"Consulta realizada com sucesso para o CPF: {e}")
        
    
    # Renderiza o formulário em caso de requisição GET
    return render(request,'./home/consulta_cpf.html')

    """
    