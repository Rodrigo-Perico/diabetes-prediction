# Diabetes Prediction

Este é um projeto de previsão de diabetes desenvolvido com Django.

---

## **Como configurar o ambiente de desenvolvimento**

### **1. Clone o repositório**
```bash
git clone https://github.com/Rodrigo-Perico/diabetes-prediction/
cd diabetes-prediction
2. Abra o projeto no VS Code
Abra o VS Code.
Navegue até a pasta do projeto:
File -> Open Folder -> Localize a pasta do projeto, por exemplo: Disco Local (C:) -> Usuários -> Seu Usuário -> diabetes-prediction.
3. Crie um ambiente virtual
No terminal do VS Code, execute:

bash
Copiar código
python -m venv venv
4. Ative o ambiente virtual
Windows:
bash
Copiar código
venv\Scripts\activate
Linux/MacOS:
bash
Copiar código
source venv/bin/activate
Você verá (venv) no início do terminal indicando que o ambiente está ativo.

5. Instale as extensões recomendadas
No VS Code:

Instale a extensão SQLite Viewer para visualizar bancos de dados SQLite.
6. Instale as dependências
No terminal, com o ambiente virtual ativo, execute:

bash
Copiar código
pip install django
pip install pickle
7. Configure o banco de dados
Aplique as migrações do Django:

bash
Copiar código
python manage.py makemigrations
python manage.py migrate
8. Execute o servidor
Inicie o servidor de desenvolvimento:

bash
Copiar código
python manage.py runserver
Acesse o projeto no navegador em: http://127.0.0.1:8000.
