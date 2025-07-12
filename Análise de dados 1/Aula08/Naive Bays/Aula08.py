from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
import pickle


# Leitura dos dados
base_risco_credito = pd.read_csv("C:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708.01/Aula08/Naive Bays/risco_credito.csv")
print(base_risco_credito)

# Previsores
X_risco_credito = base_risco_credito.iloc[:, 0:4].values
print(X_risco_credito)

# Classe
y_risco_credito = base_risco_credito.iloc[:, 4].values
print(y_risco_credito)

# Label Encoder
label_encoder_historia = LabelEncoder()
label_encoder_divida = LabelEncoder()
label_encoder_garantia = LabelEncoder()
label_encoder_renda = LabelEncoder()

X_risco_credito[:,0] = label_encoder_historia.fit_transform(X_risco_credito[:,0])
X_risco_credito[:,1] = label_encoder_divida.fit_transform(X_risco_credito[:,1])
X_risco_credito[:,2] = label_encoder_garantia.fit_transform(X_risco_credito[:,2])
X_risco_credito[:,3] = label_encoder_renda.fit_transform(X_risco_credito[:,3])

print(X_risco_credito)


# Naive Bayes começa aqui

print(label_encoder_renda.classes_)
print(label_encoder_renda.transform(['0_15'])[0])

dicionario_Renda = dict(zip(label_encoder_renda.classes_, label_encoder_renda.transform(label_encoder_renda.classes_)))

print(dicionario_Renda['0_15'])

