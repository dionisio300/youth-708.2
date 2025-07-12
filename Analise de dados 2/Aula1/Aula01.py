from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

base_risco_credito = pd.read_csv("C:/Users/dioni/OneDrive/Área de Trabalho/Youth Data 708.01/Analise de dados 2/Aula1/risco_credito.csv")

X_risco_credito = base_risco_credito.iloc[:,0:4].values
print(X_risco_credito)

Y_risco_credito = base_risco_credito.iloc[:,4].values

# Label encoder

label_encoder_historia = LabelEncoder()
label_encoder_divida = LabelEncoder()
label_encoder_garantia = LabelEncoder()
label_encoder_renda = LabelEncoder()

X_risco_credito[:,0] = label_encoder_historia.fit_transform(X_risco_credito[:,0])
X_risco_credito[:,1] = label_encoder_divida.fit_transform(X_risco_credito[:,1])
X_risco_credito[:,2] = label_encoder_garantia.fit_transform(X_risco_credito[:,2])
X_risco_credito[:,3] = label_encoder_renda.fit_transform(X_risco_credito[:,3])

print(X_risco_credito)

naive_Numerico = GaussianNB()

naive_Numerico.fit(X_risco_credito,Y_risco_credito)

print(label_encoder_historia.transform(['boa']))
print(label_encoder_divida.transform(['alta']))
print(label_encoder_garantia.transform(['nenhuma']))
print(label_encoder_renda.transform(['acima_35']))

entrada = [0,0,1,2]

resultado = naive_Numerico.predict([entrada])

print(resultado)

while True:
    opcao = input('1 - Prever\n2 - Sair\n')
    if opcao == '1':

        historia = input(f'História ( {label_encoder_historia.classes_[0]}, {label_encoder_historia.classes_[1]} ou {label_encoder_historia.classes_[2]}): ')
        divida = input(f'Divida ( {label_encoder_divida.classes_} )')
        garantias = input(f'Garantias ( {label_encoder_garantia.classes_} )')
        renda  = input(f'Renda ({label_encoder_renda.classes_})')
        

        historia = label_encoder_historia.transform([historia.lower()])[0]
        divida = label_encoder_divida.transform([divida.lower()])[0]
        garantias = label_encoder_garantia.transform([garantias.lower()])[0]
        renda = label_encoder_renda.transform([renda.lower()])[0]

        entrada = [historia,divida,garantias,renda]
        print(entrada)
        previsao = naive_Numerico.predict([entrada])
        print(f'O risco é {previsao[0]}')

    else:
        break