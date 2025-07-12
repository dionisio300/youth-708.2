Q1 = 156 # dado que está na posição de 25%
Q2 = 160 # dado que está na posição de 50%
Q3 = 164 # dado que está na posição de 75%

IQR = Q3 - Q1

limINF = Q1 - 1.5*IQR
limSUP = Q3 + 1.5* IQR

print(IQR)
print(f'Limite Inferior: {limINF}')
print(f'Limite Superior: {limSUP}')

alturas = [150,151,152,154,160,160,161,165,169,170,172,173]
rendas = [1800,1900,2000,2100,2500,2500,3000,3200,3500,4000,4500,5000]

menorAltura = min(alturas)
maiorAltura = max(alturas)

menorRenda = min(rendas)
maiorRenda = max(rendas)

amplitude = maiorAltura - menorAltura
amplitudeRenda = maiorRenda - menorRenda

alturaNormalizada = []
rendaNormalizada = []

for altura in alturas:
    valor = (altura - menorAltura)/amplitude
    alturaNormalizada.append(valor)

for renda in rendas:
    valor = (renda - menorRenda)/amplitudeRenda
    rendaNormalizada.append(valor)
print('Alturas Normalizadas: ')
print(alturaNormalizada)
print('Rendas Normalizadas: ')
print(rendaNormalizada)

import pandas as pd
import numpy as np

iris = pd.read_csv("c:/Users/dioni/OneDrive/Área de Trabalho/Youth Analise de dados/Aula04 - Análise estatística e Limpeza de dados/parte1/materiais/iris.csv")
# 
print(iris.head())

# Estatística descritiva
print('Estatística descritiva:')
print(iris.describe())

# Média:
print('Média: ')
print(iris.mean(numeric_only=True))

# Mediana
print('Mediana: ')
print(iris.median(numeric_only=True))

# Moda
print('Moda')
print(iris.mode(numeric_only=True))

# Máximo
print('Valores Máximos:')
print(iris.max(numeric_only=True))

# Mínimos
print('Valores Mínimos')
print(iris.min(numeric_only=True))

# Frequência
# print('Frequência:')
# print(iris["sepal.length"].value_counts())

###########################
#     Variabilidade   #####
###########################

# Variância
print('Variância: ')
print(iris.var(numeric_only=True))

# Desvio padrão
print('Desvio Padrão')
print(iris.std(numeric_only=True))

# Quatis e IQR

print('Quartis e IQR')
Q1 = iris.quantile(0.25,numeric_only=True)
Q2 = iris.quantile(0.5,numeric_only=True)
Q3 = iris.quantile(0.75, numeric_only=True)
print(f'Q1')
print(f'{Q1}')
print(f'Q3')
print(f'{Q3}')
print('Q2')
print(Q2)

IQR = Q3 - Q1
print('IQR')
print(IQR)

##################################
# Relacionamento entre variáveis #
##################################

# Covariância
print('Covariancia: ')
print(iris.cov(numeric_only=True))

#Correlação
print('Correlação')
print(iris.corr(numeric_only=True))

# Filtragem
setosa = iris[iris["variety"] == 'Setosa']
print(setosa)

versicolor = iris[iris["variety"] == 'Versicolor']
print(versicolor)

virginica = iris[iris["variety"] == 'Virginica']
print(virginica)

# 1. Qual espécie possui, em média, a menor largura de pétala?

mediasLarguras = [setosa["petal.length"].mean(),versicolor["petal.length"].mean(),virginica["petal.length"].mean()]

print(mediasLarguras)
print('Setosa possui a menor largura de pétala em média')

#2. Existe correlação entre o comprimento da pétala e o comprimento da sépala?

correlacaoSetosa = setosa.corr(numeric_only=True)
print(correlacaoSetosa["sepal.length"]["petal.length"])

correlacaoVeriscolor = versicolor.corr(numeric_only=True)
print(correlacaoVeriscolor["sepal.length"]["petal.length"])

correlacaoVirginica = virginica.corr(numeric_only=True)
print(correlacaoVirginica["sepal.length"]["petal.length"])

# 3. Qual das variáveis numéricas possui maior variabilidade?

varianciaSetosa = setosa.var(numeric_only=True)
print(varianciaSetosa)

varianciaVeriscolor = versicolor.var(numeric_only=True)
print(varianciaVeriscolor)

varianciaVirginica = virginica.var(numeric_only=True)
print(varianciaVirginica)

#4. Qual espécie é mais homogênea em termos de medidas (menor desvio padrão)?

varianciaSetosa = setosa.std(numeric_only=True)
print(varianciaSetosa)

varianciaVeriscolor = versicolor.std(numeric_only=True)
print(varianciaVeriscolor)

varianciaVirginica = virginica.std(numeric_only=True)
print(varianciaVirginica)

# 5. Quais variáveis seriam mais úteis para diferenciar as espécies?
print('Medias das variáveis')
print(setosa.mean(numeric_only=True))
print(virginica.mean(numeric_only=True))
print(versicolor.mean(numeric_only=True))

#6. Existe alguma espécie cujas pétalas e sépalas não têm correlação significativa?
correlacaoSetosa = setosa.corr(numeric_only=True)
print(correlacaoSetosa)
# para a setosa a correlação entre as variáveis de largura e comprimento das pétalas e sépalas não apresentam correlação alta. todas a baixo de 0.27


correlacaoVeriscolor = versicolor.corr(numeric_only=True)
print(correlacaoVeriscolor)

'''
7. Qual o intervalo interquartil (IQR) da largura da sépala da Virginica? Ele é maior ou menor que o da Setosa?

'''


'''
Questões para o dataset de vinhos

1. Qual tipo de vinho tem a maior média de teor alcoólico?

2. Existe correlação entre o teor de álcool e a cor do vinho?

3. Qual variável possui maior desvio padrão dentro de cada tipo de vinho?

4. Há alguma variável com valores extremos? Use IQR para detectar.

5. Qual tipo de vinho apresenta maior variabilidade geral?

6. Existe alguma variável fortemente correlacionada com a intensidade da cor?

7. Qual o tipo de vinho com maior concentração média de flavonoides?

8. Há correlação negativa entre alguma dupla de variáveis?

9. Após padronizar os dados, qual variável ainda apresenta grande variabilidade relativa?

10. Se você tivesse que escolher 2 variáveis para prever o tipo do vinho, quais seriam e por quê?

'''