from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

base_credit_data = pd.read_csv("C:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708.01/Analise de dados 2/Aula3/credit_data.csv")

X_credit_data = base_credit_data.iloc[:,1:4].values
print(X_credit_data)

# Normalizar os dados de entrada
from sklearn.preprocessing import MinMaxScaler
normalizacao = MinMaxScaler()
X_credit_data_normalized = normalizacao.fit_transform(X_credit_data)

Y_credit_data = base_credit_data.iloc[:,4].values
print(Y_credit_data)



# Separar dados de treino e teste
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X_credit_data_normalized, Y_credit_data, test_size=0.2, random_state=0)

# importar a biblioteca

from sklearn.neighbors import KNeighborsClassifier

# Treinamento do modelo
knn_credit = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn_credit.fit(X_train,Y_train)

# Previsões
previsoes = knn_credit.predict(X_test)

# Avaliação do modelo

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Acuracia
acuracia = accuracy_score(Y_test,previsoes)
print(acuracia)

# Classificatio report
print(classification_report(Y_test,previsoes))

# Matriz de confusão
print(f'Matriz de confusão: \n {confusion_matrix(Y_test,previsoes)}')

