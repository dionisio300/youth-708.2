from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

base_credit_data = pd.read_csv("C:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708.01/Analise de dados 2/Aula2/credit_data.csv")

X_credit_data = base_credit_data.iloc[:,1:4].values
print(X_credit_data)

Y_credit_data = base_credit_data.iloc[:,4].values
print(Y_credit_data)

# Separar dados de treino e teste
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X_credit_data, Y_credit_data, test_size=0.2, random_state=0)

# Treinar o modelo
arvore_risco_credito = DecisionTreeClassifier(criterion='entropy')
arvore_risco_credito.fit(X_train,Y_train)

previsoes = arvore_risco_credito.predict(X_test)
print(previsoes)

from sklearn.metrics import accuracy_score, classification_report
acuracia = accuracy_score(Y_test, previsoes)
print(acuracia)
print(classification_report(Y_test, previsoes))

from sklearn import tree
previsores = ['income', 'age', 'loan']
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (20,20))
tree.plot_tree(arvore_risco_credito, feature_names=previsores, class_names=['0','1'], filled=True)
plt.show()

from sklearn.ensemble import RandomForestClassifier

random_forest_credit = RandomForestClassifier(n_estimators=40, criterion='entropy', random_state = 0,)
random_forest_credit.fit(X_train, Y_train)
previsoes = random_forest_credit.predict(X_test)

print(previsoes)

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
acuracia = accuracy_score(Y_test, previsoes)
print(acuracia)

print(classification_report(Y_test, previsoes))

print(f'Matriz de confusão: \n {confusion_matrix(Y_test,previsoes)}')