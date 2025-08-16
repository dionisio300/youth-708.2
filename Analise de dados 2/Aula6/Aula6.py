# Carregar os dados do census.csv

# Label Encoder

# OneHotEncoder

# Normalização

# Aplicar os Algoritmos estudados até agora

# Naive Bayes
# Árvore de decisão
# Randon Forest
# KNN
# Regressão Logísitica
# SVM
# Redes Neurais

# Printar as acurácias de todos 
# Naive Bayes = x%
# Árvore de decisão = y%
# ...

# Aula sobre Avaliação de Algoritmos
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
# importar o Naive Bayes
from sklearn.naive_bayes import GaussianNB

# Acurácia
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Carregar os dados do census.csv

census = pd.read_csv("C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 708.01\\Materiais\\Aula6\\Aula5\\census.csv")

# Pré-processamento dos dados
# Separar os Previsores (X) da classe (y)

X_census = census.iloc[:,0:-1].values
print(X_census)

Y_census = census.iloc[:,-1].values
print(Y_census)

#label encoder: fazer uma iteração para buscar os dados categóricos e aplicar o label encoder

# LabelEncoder
from sklearn.preprocessing import LabelEncoder

labelEncoder_workclass = LabelEncoder()
labelEncoder_education = LabelEncoder()
labelEncoder_marital_status = LabelEncoder()
labelEncoder_occupation = LabelEncoder()
labelEncoder_relationship = LabelEncoder()
labelEncoder_race = LabelEncoder()
labelEncoder_sex = LabelEncoder()
labelEncoder_native_country = LabelEncoder()

X_census[:,1] = labelEncoder_workclass.fit_transform(X_census[:,1])
X_census[:,3] = labelEncoder_education.fit_transform(X_census[:,3])
X_census[:,5] = labelEncoder_marital_status.fit_transform(X_census[:,5])
X_census[:,6] = labelEncoder_occupation.fit_transform(X_census[:,6])
X_census[:,7] = labelEncoder_relationship.fit_transform(X_census[:,7])
X_census[:,8] = labelEncoder_race.fit_transform(X_census[:,8])
X_census[:,9] = labelEncoder_sex.fit_transform(X_census[:,8])
X_census[:,13] = labelEncoder_native_country.fit_transform(X_census[:,13])

print(X_census)

# OneHotEncoder

# from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer

# oneHotEncoder_census = ColumnTransformer(transformers=[('onehot', OneHotEncoder(), [1, 3, 5, 6, 7, 8, 9, 13])], remainder='passthrough')

# X_census = oneHotEncoder_census.fit_transform(X_census).toarray()

# Normalização dos dados
from sklearn.preprocessing import minmax_scale
X_census = minmax_scale(X_census)

# Separar os dados em conjuntos de treino e teste

from sklearn.model_selection import train_test_split
X_treino, X_teste, y_treino, y_teste = train_test_split(X_census, Y_census, test_size=0.2, random_state=100)


# Salvar Variáveis

import pickle

with open('census.pkl', mode = 'wb') as f:
  pickle.dump([X_treino, y_treino, X_teste, y_teste], f)

print(X_treino.shape, X_teste.shape, y_treino.shape, y_teste.shape)

# Aplicar o Naive Bayes
naive_bayes = GaussianNB()
naive_bayes.fit(X_treino, y_treino)
y_pred = naive_bayes.predict(X_teste)

# Acurácia do Naive Bayes
print("Acurácia do Naive Bayes:", accuracy_score(y_pred, y_teste))
print("Acurácia do Naive Bayes:", naive_bayes.score(X_teste, y_teste))

# Aplicar a Árvore de Decisão
arvore_decisao = DecisionTreeClassifier()
arvore_decisao.fit(X_treino, y_treino)
y_pred = arvore_decisao.predict(X_teste)

# Acurácia da Árvore de Decisão
print("Acurácia da Árvore de Decisão:", arvore_decisao.score(X_teste, y_teste))


# Aplicar o Random Forest
random_forest = RandomForestClassifier()
random_forest.fit(X_treino, y_treino)
y_pred = random_forest.predict(X_teste)

# Acurácia do Random Forest
print("Acurácia do Random Forest:", random_forest.score(X_teste, y_teste))


# Aplicar o KNN
knn = KNeighborsClassifier()
knn.fit(X_treino, y_treino)
y_pred = knn.predict(X_teste)
# Acurácia do KNN
print("Acurácia do KNN:", knn.score(X_teste, y_teste))

# Aplicar a Regressão Logística
log_reg = LogisticRegression(max_iter=1000,tol=0.001,verbose=1)
log_reg.fit(X_treino, y_treino)
y_pred = log_reg.predict(X_teste)

# Acurácia da Regressão Logística
print("Acurácia da Regressão Logística:", log_reg.score(X_teste, y_teste))


# Aplicar SVM
svm = SVC()
svm.fit(X_treino, y_treino)
y_pred = svm.predict(X_teste)

# Acurácia do SVM
print("Acurácia do SVM:", svm.score(X_teste, y_teste))


# Aplicar redes neurais

rn = MLPClassifier(max_iter=1000, tol=0.001, verbose=1)
rn.fit(X_treino, y_treino)
y_pred = rn.predict(X_teste)

# Acurácia das Redes Neurais
print("Acurácia das Redes Neurais:", rn.score(X_teste, y_teste))

# Criar um dicionário com todas as acuracias iniciais
acuracias_iniciais = {
    "Naive Bayes": round(naive_bayes.score(X_teste, y_teste),4)*100,
    "Árvore de Decisão": round(arvore_decisao.score(X_teste, y_teste),4)*100,
    "Random Forest": round(random_forest.score(X_teste, y_teste),4)*100,
    "KNN": round(knn.score(X_teste, y_teste),4)*100,
    "Regressão Logística": round(log_reg.score(X_teste, y_teste),4)*100,
    "SVM": round(svm.score(X_teste, y_teste),4)*100,
    "Redes Neurais": round(rn.score(X_teste, y_teste),4)*100
}

print("Acurácias Iniciais:")
for modelo, acuracia in acuracias_iniciais.items():
    print(f"{modelo}: {acuracia}%")


# Tuning dos Modelos
# Ajuste de Hiperparâmetros da Árvore de Decisão
# Os principais hiperparâmetros a serem ajustados são:
# - criterion, que é a função de avaliação da qualidade da divisão
# - splitter, que é a estratégia utilizada para escolher a divisão em cada nó
# - min_samples_split, que é o número mínimo de amostras necessárias para dividir um nó
# - min_samples_leaf, que é o número mínimo de amostras necessárias em um nó folha
# parametros = {'criterion': ['gini', 'entropy'],
#               'splitter': ['best', 'random'],
#               'min_samples_split': [2, 5, 10],
#               'min_samples_leaf': [1, 5, 10]
#             }

from sklearn.model_selection import GridSearchCV

# parametros_random = {
#    'criterion':['gine','entropy'],
#    'n_estimators':[10,20,30,40,50,57,60],
#    'min_samples_split':[10,100,150],
#    'min_samples_leaf':[5,6]
# }

# grid_search_random = GridSearchCV(estimator=RandomForestClassifier(),param_grid=parametros_random)
# grid_search_random.fit(X_treino,y_treino)
# print(grid_search_random.best_params_)
# print(grid_search_random.best_score_)


# parametros_arvore = {
#    'criterion':['entropy','gine','log_los'],
#    'splitter':['best','random'],
#    'min_samples_split':[200,300,400,500,600,700],
#    'min_samples_leaf':[5,6],
#    'max_depth':[4,12,14]
# }
# grid_search_arvore = GridSearchCV(estimator=DecisionTreeClassifier(),param_grid=parametros_arvore)
# grid_search_arvore.fit(X_treino,y_treino)
# print(grid_search_arvore.best_params_)
# print(grid_search_arvore.best_score_)

# Validação cruzada

from sklearn.model_selection import cross_val_score, KFold

resultados_arvore = []
resultados_random = []

for i in range (10):
   print(i)
   kFold = KFold(n_splits=5,random_state=i,shuffle=True)
   arvore = DecisionTreeClassifier(criterion='entropy',max_depth=12)
   scores = cross_val_score(arvore,X_census,Y_census,cv=kFold)
   print(scores)
   resultados_arvore.append(scores.mean())

   random = DecisionTreeClassifier(criterion='entropy',max_depth=12)
   scores = cross_val_score(random,X_census,Y_census,cv=kFold)
   print(scores)
   resultados_random.append(scores.mean())


resultados = pd.DataFrame({'Arvore':resultados_arvore, 'Random':resultados_random})

print(resultados.describe())