'''
pip install seaborn
pip install matplotlib
pip install plotly
'''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

baseCredito = pd.read_csv('C:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708.01/Aula07 - Naive Bayes e visualização de dados/credit_data.csv')

print(baseCredito)

mediaIdade = baseCredito['age'].mean()

baseCredito['age'][baseCredito['age'] < 0] = mediaIdade

# print(baseCredito.describe())
# plt.figure()
# sns.countplot(x=baseCredito['default'])
# plt.title('Pagamentos')

# plt.figure()
# plt.hist(x=baseCredito['loan'])
# plt.title('Dívida')

grafico = px.scatter_matrix(baseCredito, dimensions=['income','loan','age'], color='default')

#grafico.show()
#plt.show()

census = pd.read_csv('C:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708.01/Aula07 - Naive Bayes e visualização de dados/census.csv')

# Mostrando os dados iniciais
print(census.head())

# Contagem da renda
plt.figure()
sns.countplot(x=census['income'])
plt.title('Renda')

# histogramas
plt.figure()
plt.hist(x=census['hour-per-week'])
plt.title('Histograma da idade')

# Treemap
grafico = px.treemap(census,path=['workclass','age'])
grafico2 = px.treemap(census,path=['occupation','relationship','age'])
# grafico2.show()

# plt.show()

X_census = census.iloc[:,0:-1].values
print(X_census)

Y_census = census.iloc[:,-1].values
print(Y_census)
print(X_census[:,1])
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

# Carro
# Gol   Palio   Uno
#  1      2      3     -> LabelEncoder * 10 = 10 , 20, 30

# Gol       1 0 0    10 0  0  -> OneHotEncoder
# Palio     0 1 0    0 10  0
# Uno       0 0 1    0  0 10

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

oneHotEncoder_census = ColumnTransformer(transformers=[('onehot', OneHotEncoder(), [1, 3, 5, 6, 7, 8, 9, 13])], remainder='passthrough')

print(X_census.shape)
X_census = oneHotEncoder_census.fit_transform(X_census).toarray()

# print(X_census)
print(X_census.shape)









