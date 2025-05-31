import pandas as pd

# 1. Criando uma Series a partir de uma lista
listaNotas = [10,8,5,7]
serieNotas = pd.Series(listaNotas)

print(listaNotas)
print(serieNotas)

# 2. Definindo um índice personalizado

indices = ['a','b','c','d']
serieNotas = pd.Series(listaNotas,indices)

print(listaNotas)
print(serieNotas)

# 3. Criando a partir de um dicionário

dictAlunos = {
    "nome":"João",
    "nota" : 10,
    "Matricula":123123,
    "data":20200503
}
SerieAlunos = pd.Series(dictAlunos)

print(dictAlunos)
print(SerieAlunos)

# 4. Criando a partir de um valor escalar (repetido)

serieRepetido = pd.Series(10,[0,1,2,3,4,5])
print(serieRepetido)

# 5. Usando o parâmetro dtype name

listaAlunos = ['Ana','Maria','João']
SerieAlunos = pd.Series(listaAlunos,dtype=str,name='ListaAlunos')
print(listaAlunos)
print(SerieAlunos)

# 1. Criando um DataFramea partir de um dicionário de listas
dados = {
    "nomes":['Ana','João','Maria'],
    "idades":[23,35,31],
    "notas":[8.5,7,9.2]
}
print(dados)

dataDados = pd.DataFrame(dados)
print(dataDados)

# 2. Definindo um índice personalizado

dataDados = pd.DataFrame(dados,['a','b','c'])
print(dataDados)

# 3. Criando a partir de uma lista de dicionários
dados = [
    {"nome":"Ana","idade":23},
    {"nome":"João","idade":35,"nota":10},
    {"nome":"Maria","nota":9.2},
]

dados = pd.DataFrame(dados)
print(dados)


# 5. Com uma única Series (coluna)

listaNumeros = [10,20,30]
print(listaNumeros)
listaNumeros = pd.DataFrame(listaNumeros)
print(listaNumeros)

################################################################
######################## NumPy #################################
################################################################
import numpy as np

lista1 = [1,2,3,4,5]
lista1Dobro = []

for numero in lista1:
    dobro = numero * 2
    lista1Dobro.append(dobro)

print(lista1Dobro)

lista2 = np.array(lista1)
print(lista2)

lista2 = lista2 + 2

print(lista2)

mat1 = [[ [1,2],[3,4] ],[ [5,6],[7,8] ]] 
print(mat1)

mat2 = np.array(mat1)
print(mat2)
#print(mat2)

vetor = [1,2,3,4,5]
mat1 = [[1,2,3],[4,5,6],[7,8,9]]
cubo = [[ [1,2],[3,4] ],[ [5,6],[7,8] ]] 

vetor = np.array(vetor)
mat1 = np.array(mat1)
cubo = np.array(cubo)

# Função para saber o número de dimenções
print(vetor.ndim)
print(mat1.ndim)
print(cubo.ndim)

print(vetor.shape)
print(mat1.shape)
print(cubo.shape)

print(vetor.size)
print(mat1.size)
print(cubo.size)

matZero = np.zeros((3,3))
print(matZero + 10)

matUm = np.ones((2,2))
print(matUm)

matID = np.eye(3)
print(matID)


vetor1 = np.arange(0,1.05,0.05)
print(vetor1)

matAleatorio = np.random.rand(10, 10)
print(np.floor(matAleatorio * 101))

# 1. Crie:
# 	Um array 1D de 5 inteiros.
# 	Uma matriz 3x3 de números aleatórios inteiros entre 0 e 10.

# 2. Faça:
# 	A soma de dois arrays.
# 	A multiplicação de um array por um número.
# 	O quadrado de todos os elementos de um array.
# 3. Mostre:

# 	O número de dimensões (ndim), forma (shape), tipo (dtype) e 	a quantidade de elementos (size) de um array 2D.


# Estatística:
# amostras e população
# média, mediana, moda
# Variância, desvio padrão, desvio médio
# correlação, autocorrelação
# Matrizes






    