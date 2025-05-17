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



