import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# base_plano_saude = pd.read_csv('C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 708.01\\Analise de dados 2\\Aula7\\plano_saude.csv')

# print(base_plano_saude)

# x_plano = base_plano_saude.iloc[:,0].values
# print(x_plano)

# y_plano = base_plano_saude.iloc[:,1].values
# print(y_plano)

# print(np.corrcoef(x_plano,y_plano))

# print(x_plano.shape)
# x_plano = x_plano.reshape(-1,1)
# print(x_plano.shape)



# from sklearn.linear_model import LinearRegression
# regressor_plano_saude = LinearRegression()
# regressor_plano_saude.fit(x_plano,y_plano)
# previsoes = regressor_plano_saude.predict(x_plano)
# print(regressor_plano_saude.intercept_)
# print(regressor_plano_saude.coef_)
# print(previsoes)
# x_plano_grafico = x_plano.ravel()
# grafico = px.scatter(x=x_plano_grafico, y= y_plano)
# grafico.add_scatter(x=x_plano_grafico, y=previsoes)
# grafico.show()
# valorPrevisto = regressor_plano_saude.predict([[40]])
# print(valorPrevisto)
# print(regressor_plano_saude.score(x_plano,y_plano))

casas = pd.read_csv('C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 708.01\\Analise de dados 2\\Aula7\\house_prices.csv')

# print(casas.head())
# print(casas.describe())

casas.drop('date',axis=1, inplace=True)

# print(casas.corr())

figura = plt.figure()
sns.heatmap(casas.corr(),annot=True)
plt.show()

y_casas = casas.iloc[:,1].values
x_casas = casas.iloc[:,4].values

print(y_casas.shape)
print(x_casas.shape)

x_casas = x_casas.reshape(-1,1)
print(x_casas.shape)

# separar dados de treino e teste
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_casas, y_casas, test_size=0.2, random_state=0)

# Aplicar a regressão linear

from sklearn.linear_model import LinearRegression
regressor_casas = LinearRegression()
regressor_casas.fit(x_train, y_train)

# Fazer previsões
previsoes = regressor_casas.predict(x_train)

# plotar previsões e conjunto de dados


print(y_train.shape)

x_casas_grafico = x_train.ravel()
print('Casas Gráfico')
print(x_casas_grafico.shape)
grafico = px.scatter(x=x_casas_grafico, y= y_train)
grafico.add_scatter(x=x_casas_grafico, y=previsoes)
grafico.show()

print(regressor_casas.intercept_)
print(regressor_casas.coef_)



