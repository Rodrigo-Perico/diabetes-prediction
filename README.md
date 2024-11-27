# Diabetes Prediction

projeto de previsão de diabetes desenvolvid com Django e Machine Learning

---

## **Como configurar o Sistema**

1. Clone o repositório:
   ```yaml
   git clone https://github.com/Rodrigo-Perico/diabetes-prediction/
   cd diabetes-prediction
   ```

2. Abra o projeto no VS Code:
   - Navegue até a pasta do projeto:
     **File -> Open Folder -> Localize a pasta do projeto** (exemplo: Disco Local (C:) -> Usuários -> Seu Usuário -> diabetes-prediction).

3. Crie um ambiente virtual:
   ```yaml
   python -m venv venv
   ```

4. Ative o ambiente virtual:
   - **Windows**:
     ```yaml
     venv\Scripts\activate
     ```
   - **Linux/MacOS**:
     ```yaml
     source venv/bin/activate
     ```

5. Instale as extensões recomendadas no VS Code:
   - Instale **SQLite Viewer** (para visualizar bancos de dados SQLite).

6. Instale as dependências do projeto:
   ```yaml
   pip install django
   pip install pickle
   ```

7. Configure o banco de dados:
   ```yaml
   python manage.py makemigrations
   python.manage.py migrate
   ```

8. Execute o servidor de desenvolvimento:
   ```yaml
   python manage.py runserver
   ```

   Acesse no navegador: **http://127.0.0.1:8000**
