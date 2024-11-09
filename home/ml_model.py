import pickle

def load_model():
    with open('.//modelos/KNN.pkl', 'rb') as f:
        model = pickle.load(f)
    return model