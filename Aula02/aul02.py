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







    