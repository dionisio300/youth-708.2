from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

base_credit_data = pd.read_csv("C:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708.01/Analise de dados 2/Aula1/credit_data.csv")

X_credit_data = base_credit_data.iloc[:,1:4].values
print(X_credit_data)

Y_credit_data = base_credit_data.iloc[:,4].values
print(Y_credit_data)

# Normalizar os dados de entrada
from sklearn.preprocessing import MinMaxScaler
normalizacao = MinMaxScaler()
X_credit_data_normalized = normalizacao.fit_transform(X_credit_data)

# Separar dados de treino e teste
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X_credit_data_normalized, Y_credit_data, test_size=0.2, random_state=42)

# Treinar o modelo
naive_Numerico = GaussianNB()
naive_Numerico.fit(X_train, Y_train)

# teste para uma previsão especifica só recebendo os dados e aplicando a normalização

renda = 60000
idade = 25
divida = 13000

dadosNormalizados = normalizacao.transform([[renda,idade,divida]])
print(dadosNormalizados)

previsao = naive_Numerico.predict(dadosNormalizados)
print(previsao)

# Métricas de avaliação

from sklearn.metrics import accuracy_score, classification_report,confusion_matrix

print('Métricas de Avaliação')
Y_previsto = naive_Numerico.predict(X_test)

print(f'Acurácia: {accuracy_score(Y_test,Y_previsto)}')
print(f'Relatório de classificação: \n {classification_report(Y_test,Y_previsto)}')
print(f'Matriz de confusão: \n {confusion_matrix(Y_test,Y_previsto)}')

