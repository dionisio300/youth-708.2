from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


base_risco_credito = pd.read_csv("C:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708.01/Analise de dados 2/Aula2/risco_credito.csv")

X_risco_credito = base_risco_credito.iloc[:,0:4].values
print(X_risco_credito)

Y_risco_credito = base_risco_credito.iloc[:,4].values

# Label encoder

label_encoder_historia = LabelEncoder()
label_encoder_divida = LabelEncoder()
label_encoder_garantia = LabelEncoder()
label_encoder_renda = LabelEncoder()

X_risco_credito[:,0] = label_encoder_historia.fit_transform(X_risco_credito[:,0])
X_risco_credito[:,1] = label_encoder_divida.fit_transform(X_risco_credito[:,1])
X_risco_credito[:,2] = label_encoder_garantia.fit_transform(X_risco_credito[:,2])
X_risco_credito[:,3] = label_encoder_renda.fit_transform(X_risco_credito[:,3])

print(X_risco_credito)

# Para essa base de dados não foi necessário separar treino e teste pois a base era pequena (14 registros)
arvore_risco_credito = DecisionTreeClassifier(criterion='entropy')
arvore_risco_credito.fit(X_risco_credito,Y_risco_credito)

print(arvore_risco_credito.feature_importances_)

print(arvore_risco_credito.classes_)

from sklearn import tree

previsores = ['História','Dívida','Garantias', 'Renda']

figura, eixos = plt.subplots(nrows=1, ncols=1, figsize=(10,10))
tree.plot_tree(arvore_risco_credito,feature_names=previsores, class_names=[str(c) for c in arvore_risco_credito.classes_],filled=True)

plt.show()

print()




