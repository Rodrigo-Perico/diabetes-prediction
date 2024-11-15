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
import win32api



def load_model():
    with open('home\modelos\modelo_logistic.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def predict_diabetes(features):
    model = load_model()
    prediction = model.predict(features)
    return prediction[0]

validate_crm = RegexValidator(r'^[a-zA-Z0-9_]+$', 'O CRM deve conter apenas letras, números e underscores.')

def home(request):
    return render(request, './home/index.html')

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
            messages.error(request, "Este CRM já está registrado.")
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
            return render(request, 'Login.html')
    return render(request, './home/Login.html')

def Consulta(request):
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
        

            # Chamada da função de predição
            #prediction = predict_diabetes([features])

            # print(prediction)

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
                predict= int(prediction)
            )
            cadastro.save()

            # Exibir resultado da predição
            if prediction == 1:
                messages.success(request, "O modelo previu que o paciente pode ter diabetes.")
            else:
                messages.success(request, "O modelo previu que o paciente não tem diabetes.")
                    
        except Exception as e:
            print(e)
            messages.error(request, f"Erro ao salvar o cadastro ou realizar a predição: {e}")
            return render(request, './home/Consulta.html')
    
    return render(request, './home/Consulta.html')
