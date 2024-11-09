import pickle
import os
from django.conf import settings

# Caminho para os modelos salvos
#KNN_MODEL_PATH = os.path.join(settings.BASE_DIR, 'home', 'modelos', 'modelo_knn.pkl')
LOGISTIC_MODEL_PATH = os.path.join(settings.BASE_DIR, 'home', 'modelos', 'modelo_logistic.pkl')

# Função para carregar o modelo KNN
#def load_knn_model():
#    with open(KNN_MODEL_PATH, 'rb') as f:
#        return pickle.load(f)

# Função para carregar o modelo de Regressão Logística
def load_logistic_model():
    with open(LOGISTIC_MODEL_PATH, 'rb') as f:
        return pickle.load(f)

# Função de predição para diabetes com o modelo KNN
#def predict_diabetes_knn(features):
#    model = load_knn_model()
#    prediction = model.predict([features])
#    return prediction[0]  # Retorna o resultado da predição

# Função de predição para diabetes com o modelo de Regressão Logística
def predict_diabetes_logistic(features):
    model = load_logistic_model()
    prediction = model.predict([features])
    return prediction[0]  # Retorna o resultado da predição
