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