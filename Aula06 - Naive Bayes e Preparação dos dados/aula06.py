import pandas as pd
import numpy as np

baseCredito = pd.read_csv('C:/Users/Youth_Space_01/Desktop/Aula06/youth-708.2/Aula06 - Naive Bayes e Preparação dos dados/credit_data.csv')

# Mostrando os dados iniciais
print(baseCredito.head())

# Descrevendo a estatística geral dos dados
print(baseCredito.describe())

# Descrevendo a estatística geral dos dados
print(baseCredito.info())

# filtragem de dados negativos
print(baseCredito[baseCredito['age'] < 0])

# Substituição pela média
mediaIdade = baseCredito['age'].mean()
print(mediaIdade)

baseCredito[baseCredito['age'] < 0] = mediaIdade
print(baseCredito[baseCredito['age'] < 0])

# Preencher dados faltantes

print(baseCredito.isnull().sum())

print(baseCredito.loc[pd.isnull(baseCredito['age'])])

baseCredito['age'] = baseCredito['age'].fillna(mediaIdade)

print(baseCredito.isnull().sum())


# Divisão entre previsores e classe
# .values -> transforma o meu conjunto de dados em um array numpy

X_baseCredito = baseCredito.iloc[:,1:4].values
print(X_baseCredito)

Y_baseCredito = baseCredito.iloc[:,4].values
print(Y_baseCredito)

# pip install scikit-learn -> instalar a biblioteca de ciência da dados
from sklearn.preprocessing import MinMaxScaler

# Instância do MinMaxScaler
normalizacao = MinMaxScaler()
X_baseCredito_Normalizado = normalizacao.fit_transform(X_baseCredito)
print(X_baseCredito_Normalizado)


#Separação de dados de treino e teste
from sklearn.model_selection import train_test_split

X_baseCredito_treino, X_baseCredito_teste,Y_baseCredito_treino, Y_baseCredito_teste = train_test_split(X_baseCredito_Normalizado,Y_baseCredito, test_size=0.2, random_state=0)

print(X_baseCredito_treino.shape)
print(X_baseCredito_teste.shape)

# Opcional: Salvar os dados no formato pkl
import pickle

with open('credito.pkl', mode='wb') as f:
    pickle.dump([X_baseCredito_treino,Y_baseCredito_treino,X_baseCredito_teste,Y_baseCredito_teste], f)

# Exercício, 