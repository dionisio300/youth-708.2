from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

base_credit_data = pd.read_csv("C:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708.01/Analise de dados 2/Aula4/credit_data.csv")

X_credit_data = base_credit_data.iloc[:,1:4].values
print(X_credit_data)

imagens_treino = pd.read_csv("C:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708.01/Analise de dados 2/Aula4/mnist_train.csv")

imagens_teste = pd.read_csv("C:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708.01/Analise de dados 2/Aula4/mnist_test.csv")

x_imagens_treino = imagens_treino.iloc[:,2:-1].values
y_imagens_treino = imagens_treino.iloc[:,0].values

print(x_imagens_treino.shape)
print(y_imagens_treino.shape)

x_imagens_teste = imagens_teste.iloc[:,2:-1].values
y_imagens_teste = imagens_teste.iloc[:,0].values

print(x_imagens_teste.shape)
print(y_imagens_teste.shape)


# Normalizar os dados de entrada
from sklearn.preprocessing import MinMaxScaler
normalizacao = MinMaxScaler()
X_credit_data_normalized = normalizacao.fit_transform(X_credit_data)

Y_credit_data = base_credit_data.iloc[:,4].values
print(Y_credit_data)


# Separar dados de treino e teste
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X_credit_data_normalized, Y_credit_data, test_size=0.2, random_state=0)

from sklearn.svm import SVC

svm_credit = SVC(kernel='rbf',random_state=1,C=1)
svm_credit.fit(X_train,Y_train)

previsoes = svm_credit.predict(X_test)

svm_imagens = SVC()

svm_imagens.fit(x_imagens_treino,y_imagens_treino)

previsoes_imagens = svm_imagens.predict(x_imagens_teste)


# print(previsoes)
# print(Y_test)

# Avaliação do modelo

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Acuracia
acuracia = accuracy_score(Y_test,previsoes)
print(f'acurácia crédito = {acuracia}')

# Classificatio report
print('crédito')
print(classification_report(Y_test,previsoes))

# Matriz de confusão
print('crédito')
print(f'Matriz de confusão: \n {confusion_matrix(Y_test,previsoes)}')


# Acuracia imagens
acuracia_imagens = accuracy_score(y_imagens_teste,previsoes_imagens)
print(f'acurácia imagens = {acuracia_imagens}')

# Classificatio report
print('imagens')
print(classification_report(y_imagens_teste,previsoes_imagens))

# Matriz de confusão
print('imagens')
print(f'Matriz de confusão: \n {confusion_matrix(y_imagens_teste,previsoes_imagens)}')
