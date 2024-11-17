from django.db import models

class User(models.Model):
    CRM = models.CharField(max_length=10, primary_key=True)
    senha = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.CRM


class Cadastro(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cadastros')
    predict = models.PositiveSmallIntegerField(null=True, blank=True)
    pressao_alta = models.PositiveSmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    colesterol_alto = models.PositiveSmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    checagem_colesterol = models.PositiveSmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    imc = models.PositiveSmallIntegerField()
    fumante = models.PositiveSmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    avc = models.PositiveSmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    doencas_cardiacas = models.PositiveSmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    atividades_fisicas = models.PositiveSmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    consome_frutas = models.PositiveSmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    consome_vegetais = models.PositiveSmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    alto_consumo_alcool = models.PositiveSmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    possui_convenio = models.PositiveSmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    evitou_consultas = models.PositiveSmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    saude_geral = models.PositiveSmallIntegerField()
    saude_mental = models.PositiveSmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    saude_fisica = models.PositiveSmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    dificuldade_andar = models.PositiveSmallIntegerField(choices=[(0, 'Não'), (1, 'Sim')])
    genero = models.PositiveSmallIntegerField(choices=[(0, 'Feminino'), (1, 'Masculino')])
    cpf = models.TextField(max_length=11, unique = True)

    data_predicao = models.TextField() 
    idade = models.PositiveSmallIntegerField(choices=[
        (1, '18 a 24 anos'), (2, '25 a 29 anos'), (3, '30 a 34 anos'),
        (4, '35 a 39 anos'), (5, '40 a 44 anos'), (6, '45 a 49 anos'),
        (7, '50 a 54 anos'), (8, '55 a 59 anos'), (9, '60 a 64 anos'),
        (10, '65 a 69 anos'), (11, '70 a 74 anos'), (12, '75 a 79 anos'),
        (13, '80 a 99 anos'),
    ])
    escolaridade = models.PositiveSmallIntegerField(choices=[
        (1, 'Nunca frequentou escola ou apenas jardim de infância'),
        (2, '1ª a 8ª série (Ensino Fundamental)'),
        (3, '9ª a 11ª série (Ensino Médio incompleto)'),
        (4, '12ª série ou GED (Ensino Médio completo)'),
        (5, '1 a 3 anos de faculdade (Alguns anos de faculdade ou curso técnico)'),
        (6, '4 anos ou mais de faculdade (Diploma universitário)'),
    ])
    renda = models.PositiveSmallIntegerField(choices=[
        (1, 'Menos de R$4.166,67'), (2, 'De R$4.166,67 a menos de R$6.250,00'),
        (3, 'De R$6.250,00 a menos de R$8.333,33'), (4, 'De R$8.333,33 a menos de R$10.416,67'),
        (5, 'De R$10.416,67 a menos de R$14.583,33'), (6, 'De R$14.583,33 a menos de R$20.833,33'),
        (7, 'De R$20.833,33 a menos de R$31.250,00'), (8, 'R$31.250,00 ou mais'),
    ])


    

    def __str__(self):
        return f"Consulta de {self.user.CRM}"


 #CRIAR TABELA DE PREDIÇÃO DE MODO A SALVAR INFORMAÇÕES DE TUDO!
from django.db import models

"""
# Modelo para armazenar informações de predições
class Predicao(models.Model):
    crm_medico = models.CharField(max_length=50)  # CRM do médico (sem ser primary_key aqui)
    cpf_paciente = models.CharField(max_length=11)  # CPF do paciente
    data_predicao = models.CharField(max_length=10)  # Data da predição (melhor usar DateField se possível)
    nome_paciente = models.CharField(max_length=50)  # Nome do paciente
    modelo = models.CharField(max_length=20)  # Nome do modelo de IA usado
    predict = models.PositiveSmallIntegerField(null=True, blank=True)  # Resultado da predição (ex.: 0 ou 1)
    metricas = 

    # Relacionamento com outro modelo (Exemplo: médico)
    cpf_paciente_fk = models.ForeignKey(
        'Consulta',  # Supondo que você tenha uma tabela chamada 'Medico'
        on_delete=models.CASCADE,  # Apaga as predições se o médico for deletado
        related_name='predicoes',  # Nome reverso para consultas
    )

    def __str__(self):
        return f'Predição para {self.nome_paciente} pelo médico {self.crm_medico}'

"""


