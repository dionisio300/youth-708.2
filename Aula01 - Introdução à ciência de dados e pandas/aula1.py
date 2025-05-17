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

# 2. Dada a lista de notas de alunos, calcule a média apenas dos alunos que tiraram nota maior ou igual a 7
notas = [5.5, 8.2, 6.0, 7.0, 9.5, 3.0, 7.5]
# Resultado esperado: média das notas maiores ou iguais a 7

# 3. Escreva uma função que recebe uma lista de notas e retorna:
# a média e o conceito (A: >= 9, B: >= 7, C: >= 5, D: <5)
def analisar_notas(lista_notas):
    pass
# Exemplo:
# analisar_notas([7, 8, 9]) → (8.0, "B")

# 4. Dada a lista de notas de alunos, calcule a média apenas dos alunos que tiraram nota maior ou igual a 7
notas = [5.5, 8.2, 6.0, 7.0, 9.5, 3.0, 7.5]
# Resultado esperado: média das notas maiores ou iguais a 7

# 5. Dada uma lista de dicionários com informações de pessoas, calcule a média das idades.

dados = [
    {"nome": "Ana", "idade": 23},
    {"nome": "Bruno", "idade": 25},
    {"nome": "Carlos", "idade": 30},
    {"nome": "Diana", "idade": 20}
]
# Resultado esperado: média das idades (24.5)
# Exemplo:
# analisar_notas([7, 8, 9]) → (8.0, "B")

# 6. A partir da mesma lista acima, filtre apenas as pessoas com idade acima de 24.



