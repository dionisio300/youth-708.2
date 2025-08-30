import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import plotly.io as pio
pio.renderers.default = "browser"  # abre no navegador padrão


base_plano_saude = pd.read_csv("C:\\Users\\dioni\\OneDrive\\Área de Trabalho\\Youth Data 708.01\\Analise de dados 2\\Aula7Reposicao\\plano_saude.csv")
print(base_plano_saude.head())

# Separar variáveis independentes e dependentes
y_plano_saude = base_plano_saude["custo"].values
X_plano_saude = base_plano_saude["idade"].values

print(X_plano_saude)
print(y_plano_saude)

correlacao = np.corrcoef(X_plano_saude, y_plano_saude)
print(correlacao)

print(X_plano_saude.shape)
X_plano_saude = X_plano_saude.reshape(-1, 1)
print(X_plano_saude.shape)

# treinamento do modelo de regressão linear
from sklearn.linear_model import LinearRegression

regressaoLinearSaude = LinearRegression()
regressaoLinearSaude.fit(X_plano_saude, y_plano_saude)

print(regressaoLinearSaude.coef_)
print(regressaoLinearSaude.intercept_)

previsoes = regressaoLinearSaude.predict(X_plano_saude)
print(y_plano_saude)
print(previsoes.round(2))

grafico = px.scatter(x = X_plano_saude.ravel(), y = y_plano_saude)
grafico.add_scatter(x = X_plano_saude.ravel(), y = previsoes, name = 'Regressão')
grafico.show()

idade = int(input("Digite a idade para prever o custo: "))
custo_previsto = regressaoLinearSaude.predict(np.array([[idade]]))
print(f"O custo previsto para a idade {idade} é: {custo_previsto[0]:.2f}")