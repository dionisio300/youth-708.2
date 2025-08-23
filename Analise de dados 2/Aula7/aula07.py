import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

base_plano_saude = pd.read_csv('C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 708.01\\Analise de dados 2\\Aula7\\plano_saude.csv')

print(base_plano_saude)

x_plano = base_plano_saude.iloc[:,0].values
print(x_plano)

y_plano = base_plano_saude.iloc[:,1].values
print(y_plano)

print(np.corrcoef(x_plano,y_plano))

print(x_plano.shape)
x_plano = x_plano.reshape(-1,1)
print(x_plano.shape)

# y_plano = y_plano.reshape(-1,1)
# print(y_plano.shape)

from sklearn.linear_model import LinearRegression
regressor_plano_saude = LinearRegression()
regressor_plano_saude.fit(x_plano,y_plano)
previsoes = regressor_plano_saude.predict(x_plano)
print(regressor_plano_saude.intercept_)
print(regressor_plano_saude.coef_)
print(previsoes)
x_plano_grafico = x_plano.ravel()
grafico = px.scatter(x=x_plano_grafico, y= y_plano)
grafico.add_scatter(x=x_plano_grafico, y=previsoes)
grafico.show()
valorPrevisto = regressor_plano_saude.predict([[40]])
print(valorPrevisto)
print(regressor_plano_saude.score(x_plano,y_plano))
