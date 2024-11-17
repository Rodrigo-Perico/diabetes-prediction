# Diabetes Prediction

Este é um projeto de previsão de diabetes desenvolvido com Django.

---

## **Como configurar o ambiente de desenvolvimento**

1. Clone o repositório:
   ```bash
   git clone https://github.com/Rodrigo-Perico/diabetes-prediction/
   cd diabetes-prediction
Abra o projeto no VS Code:

Navegue até a pasta do projeto: File -> Open Folder -> Localize a pasta do projeto (exemplo: Disco Local (C:) -> Usuários -> Seu Usuário -> diabetes-prediction).
Crie um ambiente virtual:

bash
Copiar código
python -m venv venv
Ative o ambiente virtual:

Windows:
bash
Copiar código
venv\Scripts\activate
Linux/MacOS:
bash
Copiar código
source venv/bin/activate
Instale as extensões recomendadas no VS Code:

SQLite Viewer (para visualizar bancos de dados SQLite).
Instale as dependências do projeto:

bash
Copiar código
pip install django
pip install pickle
Configure o banco de dados:

bash
Copiar código
python manage.py makemigrations
python manage.py migrate
Execute o servidor de desenvolvimento:

bash
Copiar código
python manage.py runserver
Acesse no navegador: http://127.0.0.1:8000
