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

iris = pd.read_csv("c:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708/Data 1/Aula04 - Análise estatística e Limpeza de dados/parte1/materiais/iris.csv")

# 
print(iris.head())

# Estatística descritiva
print('Estatística descritiva:')
print(iris.describe())

# Média:
print('Média: ')
print(iris.mean(numeric_only=True))










