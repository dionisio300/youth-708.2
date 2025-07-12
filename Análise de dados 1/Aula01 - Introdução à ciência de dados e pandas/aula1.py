# Funções
def somar_numeros(a, b):
    print(a + b)
    return a+b

def descrever_pessoa(pessoas):
    for pessoa in pessoas:
        print(f'{pessoa["nome"]} tem {pessoa["idade"]} anos e mora em {pessoa["cidade"]}')

# Revisão de python

# Listas - Lista de nomes

#          0       1         2       3
nomes = ['Ana','Beatriz','Carlos','Davi']
print(nomes)
print(nomes[2])

# Percorrendo uma lista
for nome in nomes:
    print(f'Olá {nome}')

for i in range (len(nomes)):
    print(f'Oi {nomes[i]}')

print(len(nomes))

# Dicionários

pessoa = {
    "nome":"Ana",
    "idade":23,
    "cidade":"São Paulo"
}

print(pessoa)
print(pessoa["nome"])

print(f'A {pessoa['nome']} tem {pessoa['idade']} anos e mora em {pessoa['cidade']}')

# Lista de dicionários

pessoas = [
    {'nome':'Ana', 'idade':35, 'cidade':'São Paulo'},
    {'nome':'Egberto', 'idade':34, 'cidade':'Fortaleza'},
    {'nome':'Julio', 'idade':13, 'cidade':'Baturité'},
    {'nome':'Dionizio', 'idade':28, 'cidade':'Fortaleza'}
]



pessoa = {'nome':'Larissa', 'idade':20, 'cidade':'Fortaleza'}

pessoas.append(pessoa)

print(pessoas)

# resultado = 25
resultado = somar_numeros(10,15)

descrever_pessoa(pessoas)

# Métodos de string
string1 = 'Olá Mundo'
print(string1)

string1 = string1.upper()
print(string1)

string1 = string1.lower()
print(string1)




#Exercícios

# 1. Dada a lista de nomes, crie uma nova lista com apenas os nomes com mais de 5 letras
nomes = ["Ana", "Bruno", "Carla", "Daniela", "Eva", "Fernanda", "Igor"]
# Resultado esperado: ["Bruno", "Carla", "Daniela", "Fernanda"]

#Resposta:
nomes2 = []
for nome in nomes:
    if len(nome) >= 5:
        nomes2.append(nome)

print(nomes2)

# 2. Dada a lista de notas de alunos, calcule a média apenas dos alunos que tiraram nota maior ou igual a 7
notas = [5.5, 8.2, 6.0, 7.0, 9.5, 3.0, 7.5]
# Resultado esperado: média das notas maiores ou iguais a 7

#Resposta
soma = 0
quantidade = 0
for nota in notas:
    if nota >=7:
        soma += nota
        quantidade += 1

media = soma/quantidade

print(f'A média de quem passou é {media}')

# 3. Escreva uma função que recebe uma lista de notas e retorna:
# a média e o conceito (A: >= 9, B: >= 7, C: >= 5, D: <5)
def analisar_notas(lista_notas):
    soma = 0
    quantidade = 0
    conceito = ''

    for nota in lista_notas:
        soma += nota
        quantidade += 1

    media = soma/quantidade

    if media >= 9:
        conceito = 'A'
    elif media < 9 and media >=7:
        conceito = 'B'
    elif media < 7 and media >=5:
        conceito = 'C'
    elif media < 5:
        conceito = 'D'
    
    return media, conceito


[m, c] = analisar_notas(notas)

print(f'A sua média é {m:.2f} e o conceito foi {c}')

# Exemplo:
# analisar_notas([7, 8, 9]) → (8.0, "B")


# 4. Dada uma lista de dicionários com informações de pessoas, calcule a média das idades.

dados = [
    {"nome": "Ana", "idade": 23},
    {"nome": "Bruno", "idade": 25},
    {"nome": "Carlos", "idade": 30},
    {"nome": "Diana", "idade": 20}
]
# Resultado esperado: média das idades (24.5)
# Exemplo:
# analisar_notas([7, 8, 9]) → (8.0, "B")
soma = 0
quantidade = 0

for dado in dados:
    soma += dado['idade']
    quantidade += 1

media = soma/quantidade
print(f'A média das idades é {media}')

# 5. A partir da mesma lista acima, filtre apenas as pessoas com idade acima de 24.


for dado in dados:
    if dado['idade'] >= 24:
        print(f"Nome: {dado['nome']} - Idade: {dado['idade']}")


# instalação da biblioteca do Pandas
# pip install pandas

import pandas as pd

# 1. Criando uma Series a partir de uma lista

lista_notas = [10 , 8, 7]

serie_notas = pd.Series(lista_notas)
print(serie_notas)



# 2. Definindo um índice personalizado

indices = ['A','B','C']

serie_notas = pd.Series(lista_notas,indices)
print(serie_notas)


# 3. Criando a partir de um dicionário

serie_dados = pd.Series(dados)
print(serie_dados)

# 4. Criando a partir de um valor escalar (repetido)

serie1 = pd.Series(5,[0,1,2,3,4,5])
print(serie1)

# 5. Usando o parâmetro dtype e name

serie2 = pd.Series(data=lista_notas,index = indices,dtype='int64',name='notas')
print(serie2)

# Exemplos de DataFrame
# 1. Criando um DataFrame a partir de um dicionário de listas

dados = {
    "nomes":['Ana','João','Maria'],
    "idade":[23,35,31],
    "notas":[8.5, 7, 9.2]
}

dataFrameDados = pd.DataFrame(dados)
print(dataFrameDados)

# 2. Definindo um índice personalizado
indices = ['A','B','C']

dataFrameDados2 = pd.DataFrame(dados,indices)
print(dataFrameDados2)

# 3. Criando a partir de uma lista de dicionários

dados = [
    {"nome":"Ana", "idade": 23, "nota":10},
    {"nome":"João", "idade": 35, "nota":8},
    {"nome":"Pedro", "idade": 23, "nota":6},
]

dataFrameDados3 = pd.DataFrame(dados)
print(dataFrameDados3)

# 5. Com uma única Series (coluna)
lista_notas = [10 , 8, 7]

dataFrameDados4 = pd.DataFrame(lista_notas,[1,2,3])
print(dataFrameDados4)

'''
Atividades :

Atividade 1: Crie uma lista com os nomes de cinco frutas e transforme essa lista em uma Series do pandas.

Atividade 2: Crie uma lista com os valores de temperatura ao longo de 7 dias. Crie uma Series que use os dias da semana como índice.

Atividade 3: Crie uma Series usando um dicionário onde as chaves são nomes de alunos e os valores são suas notas finais.

Atividade 4: Crie uma Series com os números de 1 a 5 e defina índices personalizados em formato de letras.

Atividade 5: Crie um dicionário com os dados de três pessoas contendo nome, idade e cidade. Use esse dicionário para criar um DataFrame.

Atividade 6: Crie uma lista de dicionários representando três livros, com as chaves: "título", "autor", "ano". Use essa lista para criar um DataFrame.

Atividade 7: Crie um DataFrame a partir de uma lista de listas. Os dados devem representar [nome, idade] de três pessoas. Defina os nomes das colunas como "Nome" e "Idade".

Atividade 8: Crie um DataFrame usando um array do NumPy com números inteiros de 1 a 9, em uma matriz 3x3. Defina os nomes das colunas como "A", "B", "C".

Atividade 9: Crie um DataFrame a partir de um dicionário de Series. Cada chave do dicionário deve representar uma coluna.

'''



