from sklearn.naive_bayes import GaussianNB

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
import pickle


base_risco_credito = pd.read_csv("C:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708.01/Aula08/Naive Bays/risco_credito.csv")

print(base_risco_credito)

X_risco_credito = base_risco_credito.iloc[:, 0:4].values

print(X_risco_credito)

y_risco_credito = base_risco_credito.iloc[:, 4].values
print(y_risco_credito)

label_encoder_historia = LabelEncoder()
label_encoder_divida = LabelEncoder()
label_encoder_garantia = LabelEncoder()
label_encoder_renda = LabelEncoder()

X_risco_credito[:,0] = label_encoder_historia.fit_transform(X_risco_credito[:,0])
X_risco_credito[:,1] = label_encoder_divida.fit_transform(X_risco_credito[:,1])
X_risco_credito[:,2] = label_encoder_garantia.fit_transform(X_risco_credito[:,2])
X_risco_credito[:,3] = label_encoder_renda.fit_transform(X_risco_credito[:,3])

print(X_risco_credito)

with open('risco_credito.pkl', 'wb') as f:
  pickle.dump([X_risco_credito, y_risco_credito], f)


# Naive Bayes começa aqui


naive_risco_credito = GaussianNB()
naive_risco_credito.fit(X_risco_credito, y_risco_credito)


# história boa (0), dívida alta (0), garantias nenhuma (1), renda > 35 (2)
# história ruim (2), dívida alta (0), garantias adequada (0), renda < 15 (0)
previsao = naive_risco_credito.predict([[0,0,1,2], [2,0,0,0]])

print(previsao)

print(naive_risco_credito.classes_)


print("Histórico:", label_encoder_historia.classes_)
print("Dívida:", label_encoder_divida.classes_)
print("Garantia:", label_encoder_garantia.classes_)
print("Renda:", label_encoder_renda.classes_)

print(dict(zip(label_encoder_historia.classes_, label_encoder_historia.transform(label_encoder_historia.classes_))))

print("Classes:", naive_risco_credito.classes_)
print("Médias por classe:\n", naive_risco_credito.theta_)  # média de cada atributo por classe
print("Variâncias por classe:\n", naive_risco_credito.var_) # variância de cada atributo por classe
print("Probabilidades a priori:", naive_risco_credito.class_prior_)  # probabilidade de cada classe

while True:
    print("\nDigite os dados para previsão de risco de crédito (ou 'sair' para encerrar):")

    historia_input = input(f"Histórico ({', '.join(label_encoder_historia.classes_)}): ")
    if historia_input.lower() == 'sair':
        break

    divida_input = input(f"Dívida ({', '.join(label_encoder_divida.classes_)}): ")
    if divida_input.lower() == 'sair':
        break

    garantia_input = input(f"Garantia ({', '.join(label_encoder_garantia.classes_)}): ")
    if garantia_input.lower() == 'sair':
        break

    renda_input = input(f"Renda ({', '.join(label_encoder_renda.classes_)}): ")
    if renda_input.lower() == 'sair':
        break

    try:
        entrada = [
            label_encoder_historia.transform([historia_input])[0],
            label_encoder_divida.transform([divida_input])[0],
            label_encoder_garantia.transform([garantia_input])[0],
            label_encoder_renda.transform([renda_input])[0]
        ]

        resultado = naive_risco_credito.predict([entrada])[0]
        print(f"Risco de crédito previsto: {resultado}")

    except Exception as e:
        print("Erro ao processar entrada. Verifique os valores digitados.")
        print(e)
