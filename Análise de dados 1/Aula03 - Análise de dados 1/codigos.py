'''
pip install numpy pandas
'''
import pandas as pd

notas = pd.read_csv("Materiais/notas_alunos.csv")
#vendas = pd.read_csv('Materiais/vendas_loja.csv')

#print(notas)

# Tamanho da população
qtdAlunos = len(notas)
print(f'A população é composta por {qtdAlunos} alunos')

# Amostragem aleatória de dados
amostraAlunos = notas.sample(10, random_state=40)
print('Amostra de 10 alunos')
print(amostraAlunos)

# Frequência absoluta
genero = notas['Sexo'].value_counts()
print(genero)

# Frequência relativa
genero = notas['Sexo'].value_counts(normalize=True) * 100
print(genero)

# Frequência absoluta
presenca = notas['Presenca'].value_counts()
print(presenca)

# Medidas de Tendência Central

# Média

mediaTurmaP1 = notas['Nota_P1'].mean()
print(f'A média da turma foi {mediaTurmaP1}')

mediaAmostraP1 = amostraAlunos['Nota_P1'].mean()
print(f'A média das amostras é {mediaAmostraP1}')

# Mediana

medianaTurmaP1 = notas['Nota_P1'].median()
print(f"A mediana da turama é {medianaTurmaP1}")

medianaAmostraP1 = amostraAlunos['Nota_P1'].median()
print(f'A mediana da turma é {medianaAmostraP1}')

# Moda

modaTurmaP1 = notas['Nota_P1'].mode()
print(f"A Moda da turama é {medianaTurmaP1}")

modaAmostraP1 = amostraAlunos['Nota_P1'].mode()
print(f'A Moda da turma é {medianaAmostraP1}')

# 25%
Q1 = 2.5
# 50%
Q2 = 7.5
#75%
Q3 = 12.5

IQR = Q3 - Q1 #10




