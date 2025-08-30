import plotly.express as px
import plotly as plt
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.io as pio
pio.renderers.default = "browser"  # abre no navegador padrão

base_plano_saude = pd.read_csv('C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 708.01\\Analise de dados 2\\Aula8\\plano_saude.csv')

x_plano_saude = base_plano_saude.iloc[:,0].values
print(x_plano_saude.shape)


y_plano_saude = base_plano_saude.iloc[:,1].values

print(np.corrcoef(x_plano_saude,y_plano_saude))

x_plano_saude = x_plano_saude.reshape(-1,1)
print(x_plano_saude.shape)

# regressão linear

from sklearn.linear_model import LinearRegression
regressao_plano = LinearRegression()
regressao_plano.fit(x_plano_saude,y_plano_saude)

previsoes = regressao_plano.predict(x_plano_saude)

print(y_plano_saude)
print(previsoes.round(1))

grafico= px.scatter(x = x_plano_saude.ravel(), y = y_plano_saude)
grafico.add_scatter(x=x_plano_saude.ravel(), y = previsoes)
grafico.show()

# idade = int(input('Digite a sua idade: '))
# previsao = regressao_plano.predict([[idade]])

# print(f'O valor do seu plano de saúde é {previsao[0]}')

from sklearn.metrics import r2_score
r2L = r2_score(y_plano_saude,previsoes)
print(f'R2 Linear = {r2L}')


# Regressão Polinomial


from sklearn.preprocessing import PolynomialFeatures
grau = 5
poly = PolynomialFeatures(degree=grau)
x_plano_saude2 = poly.fit_transform(x_plano_saude)
print(x_plano_saude)
print(x_plano_saude2.round(1))

regressor_saude_polinomial = LinearRegression()
regressor_saude_polinomial.fit(x_plano_saude2,y_plano_saude)


previsoes2 = regressor_saude_polinomial.predict(x_plano_saude2)

# print(y_plano_saude)
# print(previsoes2.round(2))

grafico= px.scatter(x = x_plano_saude2[:,1], y = y_plano_saude)
grafico.add_scatter(x = x_plano_saude2[:,1], y = previsoes2)
# grafico.show()

r2L = r2_score(y_plano_saude,previsoes2)
print(f'R2 Poli({grau}) = {r2L}')

# idade = int(input('Idade: '))
# idade = [[idade]]
# idade = poly.transform(idade)
# print(idade)

# valorPlano = regressor_saude_polinomial.predict(idade)
# print(f'Valor do plano: {valorPlano}')


# Regressão por Árvore de Decisão

from sklearn.tree import DecisionTreeRegressor
regressao_arvore = DecisionTreeRegressor()
regressao_arvore.fit(x_plano_saude,y_plano_saude)

previsoesArvore = regressao_arvore.predict(x_plano_saude)
# print(y_plano_saude)
# print(previsoesArvore)

x_teste_arvore = np.arange(min(x_plano_saude), max(x_plano_saude), 0.1)
# print(x_teste_arvore)

x_teste_arvore1 = x_teste_arvore.reshape(-1,1)
y_teste_arvore = regressao_arvore.predict(x_teste_arvore1)

grafico= px.scatter(x = x_plano_saude.ravel(), y = y_plano_saude)
grafico.add_scatter(x = x_teste_arvore, y = y_teste_arvore)
# grafico.show()

r2L = r2_score(y_plano_saude,previsoesArvore)
print(f'R2 Árvore = {r2L}')

from sklearn.ensemble import RandomForestRegressor
regressorRandomForest = RandomForestRegressor(n_estimators=100)
regressorRandomForest.fit(x_plano_saude,y_plano_saude)

previsaoRandomForest = regressorRandomForest.predict(x_plano_saude)
# print(y_plano_saude)
# print(previsaoRandomForest)
y_teste_randomForest = regressorRandomForest.predict(x_teste_arvore1)
r2L = r2_score(y_plano_saude,previsaoRandomForest)
print(f'R2 Random Forest = {r2L}')

grafico= px.scatter(x = x_plano_saude.ravel(), y = y_plano_saude)
grafico.add_scatter(x = x_teste_arvore, y = y_teste_randomForest)
# grafico.show()

# SVM

from sklearn.svm import SVR
regressor_svr_saude = SVR(kernel='poly')
regressor_svr_saude.fit(x_plano_saude,y_plano_saude)

previsao_SVM = regressor_svr_saude.predict(x_plano_saude)

r2L = r2_score(y_plano_saude,previsao_SVM)
print(f'R2 SVM = {r2L}')


print(y_plano_saude)
print(previsao_SVM)

# Redes Neurais

from sklearn.neural_network import MLPRegressor

regressao_Redes_Neurais = MLPRegressor(hidden_layer_sizes=(10,10),max_iter=10000)
regressao_Redes_Neurais.fit(x_plano_saude,y_plano_saude)

previsao_MLP = regressao_Redes_Neurais.predict(x_plano_saude)
print(y_plano_saude)
print(previsao_MLP)

r2L = r2_score(y_plano_saude,previsao_MLP)
print(f'R2 MLP = {r2L}')
