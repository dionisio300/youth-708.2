import pandas as pd

dados = pd.read_csv("C:/Users/dioni/OneDrive/Área de Trabalho/Youth Analise de dados/Aula05 - Pré processamento de dados/iris2.csv")

print(dados.head(10))
print(dados.info())
print(dados.describe())


dados['species'] = dados['species'].astype(str)

# print(dados['sepal length (cm)'].astype(int))

# função para identificar dados faltantes
print(dados.isnull().sum())


# Remover as linhas ou colunas com valores nulos

# dropna(axis=0(linhas)1(colunas), how=(any - remove se tiver qualquer nulo) 'all' Remove se tiver tods os valores nulos)

data2 = dados.dropna(axis=0,how='any')
print(data2.isnull().sum())
print(data2.describe())

# fillna(valor) -> preenche os valores faltantes

# dados.fillna(0,inplace=True)

print(dados.isnull().sum())

sepalLengthMedia = dados['sepal length (cm)'].mean()
sepalWidthMedia = dados['sepal width (cm)'].mean()
petalLenMedia = dados['petal length (cm)'].mean()

print(sepalLengthMedia,sepalWidthMedia,petalLenMedia)
dados['sepal length (cm)'].fillna(sepalLengthMedia, inplace=True)
dados['sepal width (cm)'].fillna(sepalWidthMedia, inplace=True)
dados['petal length (cm)'].fillna(petalLenMedia, inplace=True)

print(dados.isnull().sum())
print(dados.describe())
medias = dados.mean(numeric_only=True)
print(medias)

# Filtragem de dados

dadosSetosa = dados[(dados['species'] == 'setosa') & (dados['petal length (cm)'] > 0) & (dados['petal width (cm)'] > 0)]

dadosVirginica = dados[dados['species'] == 'virginica']

dadosVeriscolor = dados[dados['species'] == 'versicolor']
print('Setosa: ')
print(dadosSetosa.describe())
print('Virginica: ')
print(dadosVirginica.describe())
print('Veriscolor: ')
print(dadosVeriscolor.describe())

Q1 = dadosVeriscolor['petal width (cm)'].quantile(0.25)
Q3 = dadosVeriscolor['petal width (cm)'].quantile(0.75)

IQR = Q3-Q1
limSup = Q3 + 1.5*IQR
limInf = Q1-1.5*IQR

outliers = dadosVeriscolor[(dadosVeriscolor['petal width (cm)'] > limSup) | (dadosVeriscolor['petal width (cm)'] < limInf)]

print(outliers)

print(dadosVeriscolor[dadosVeriscolor['petal width (cm)'] < limSup].describe())

print(dadosSetosa.loc[0:5,'sepal length (cm)'])
print(dadosSetosa.iloc[0:5,0])

dadosVeriscolor.loc[dadosVeriscolor['petal width (cm)'] > limSup,'petal width (cm)'] = limSup

# print(dadosVeriscolor.loc[50])
# for i in range (50):
#     for j in range (4):
#         dadosVeriscolor.iloc[i,j]
print(dadosVeriscolor.sort_values('sepal length (cm)').sort_index())