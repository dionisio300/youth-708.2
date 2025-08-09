from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

base_credit_data = pd.read_csv("C:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708.01/Analise de dados 2/Aula4/credit_data.csv")

X_credit_data = base_credit_data.iloc[:,1:4].values
# print(X_credit_data)

Y_credit_data = base_credit_data.iloc[:,4].values
# print(Y_credit_data)

# Normalizar os dados de entrada
from sklearn.preprocessing import MinMaxScaler
normalizacao = MinMaxScaler()
X_credit_data_normalized = normalizacao.fit_transform(X_credit_data)

# Separar dados de treino e teste
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X_credit_data_normalized, Y_credit_data, test_size=0.2, random_state=0)

# Redes Neurais

from sklearn.neural_network import MLPClassifier
rede_neural_credit = MLPClassifier(max_iter=1500,verbose=False,tol=0.000001,solver='adam',activation='relu',hidden_layer_sizes=(20,20,20), random_state=1)

rede_neural_credit.fit(X_train,Y_train)


previsoes_rede_neural = rede_neural_credit.predict(X_test)

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# Acuracia
acuracia_rede_neural = accuracy_score(Y_test,previsoes_rede_neural)
print(f'acurácia Redes Neurais = {acuracia_rede_neural}')
# Classificatio report
# print('crédito')
# print(classification_report(Y_test,previsoes_rede_neural))
# # Matriz de confusão
# print('crédito')
# print(f'Matriz de confusão: \n {confusion_matrix(Y_test,previsoes_rede_neural)}')

# SVM

from sklearn.svm import SVC

svm_credit = SVC(kernel='rbf',random_state=1,C=1)
svm_credit.fit(X_train,Y_train)
previsoes_svm = svm_credit.predict(X_test)

# Acuracia
acuracia_svm = accuracy_score(Y_test,previsoes_svm)
print(f'acurácia SVM = {acuracia_svm}')

# # Classificatio report
# print('crédito')
# print(classification_report(Y_test,previsoes_svm))

# # Matriz de confusão
# print('crédito')
# print(f'Matriz de confusão: \n {confusion_matrix(Y_test,previsoes_svm)}')


from sklearn.neighbors import KNeighborsClassifier

# Treinamento do modelo
knn_credit = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn_credit.fit(X_train,Y_train)

# Previsões
previsoes_knn = knn_credit.predict(X_test)

# Acuracia
acuracia_knn = accuracy_score(Y_test,previsoes_knn)
print(f'acurácia knn = {acuracia_knn}')

# # Classificatio report
# print(classification_report(Y_test,previsoes_knn))

# # Matriz de confusão
# print(f'Matriz de confusão: \n {confusion_matrix(Y_test,previsoes_knn)}')

# importar a biblioteca
from sklearn.linear_model import LogisticRegression

# Fazer o treinamento
regressaoLogistica = LogisticRegression(max_iter=50,solver="lbfgs")
regressaoLogistica.fit(X_train,Y_train)

# Previsões
previsoes_logistica = regressaoLogistica.predict(X_test)

# Acuracia
acuracia_logistica = accuracy_score(Y_test,previsoes_logistica)
print(f'acurácia Logistica = {acuracia_logistica}')

# # Classificatio report
# print(classification_report(Y_test,previsoes_knn))

# # Matriz de confusão
# print(f'Matriz de confusão: \n {confusion_matrix(Y_test,previsoes_knn)}')





