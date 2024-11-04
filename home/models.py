from django.db import models

class User(models.Model):
    CRM = models.CharField(max_length=50)
    senha = models.CharField(max_length=16, default='')
    
    
class Cadastro(models.Model):
    # Campos do modelo
    pressao_alta = models.CharField(max_length=3)  # Ex: "Sim" ou "Não"
    colesterol_alto = models.CharField(max_length=3)  # Ex: "Sim" ou "Não"
    checagem_colesterol = models.CharField(max_length=3)  # Ex: "Sim" ou "Não"
    imc = models.FloatField()  # Índice de Massa Corporal
    fumante = models.CharField(max_length=3)  # Ex: "Sim" ou "Não"
    avc = models.CharField(max_length=3)  # Ex: "Sim" ou "Não"
    doencas_cardiacas = models.CharField(max_length=3)  # Ex: "Sim" ou "Não"
    atividades_fisicas = models.CharField(max_length=3)  # Ex: "Sim" ou "Não"
    consome_frutas = models.CharField(max_length=3)  # Ex: "Sim" ou "Não"
    consome_vegetais = models.CharField(max_length=3)  # Ex: "Sim" ou "Não"
    alto_consumo_alcool = models.CharField(max_length=3)  # Ex: "Sim" ou "Não"
    possui_convenio = models.CharField(max_length=3)  # Ex: "Sim" ou "Não"
    evitou_consultas = models.CharField(max_length=3)  # Ex: "Sim" ou "Não"
    saude_geral = models.IntegerField()  # Saúde Geral (número de 1 a 5, por exemplo)
    saude_mental = models.CharField(max_length=3)  # Ex: "Sim" ou "Não"
    saude_fisica = models.CharField(max_length=3)  # Ex: "Sim" ou "Não"
    dificuldade_andar = models.CharField(max_length=3)  # Ex: "Sim" ou "Não"
    genero = models.IntegerField()  # Gênero (0 para feminino, 1 para masculino)
    idade = models.IntegerField()  # Idade
    escolaridade = models.CharField(max_length=50)  # Escolaridade
    renda = models.CharField(max_length=50)  # Renda"