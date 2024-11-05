import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Carregar a base de dados do diabetes
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# Pré-processamento dos dados (normalização, por exemplo)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo (usando regressão logística como exemplo)
model = LogisticRegression()
model.fit(X_train, y_train)

# Testar a acurácia
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {accuracy:.2f}')

# Agora, vamos salvar o modelo em um arquivo .pkl
with open('diabetes_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Modelo salvo com sucesso em 'diabetes_model.pkl'.")
