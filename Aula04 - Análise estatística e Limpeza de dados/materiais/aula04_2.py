# 📦 Importações
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from scipy import stats

# 📥 Carregar o dataset Iris
iris = load_iris(as_frame=True)
df = iris.frame
df.rename(columns={"target": "species"}, inplace=True)
df["species"] = df["species"].map(dict(enumerate(iris.target_names)))

print("✅ Dataset carregado:")
print(df.head())

# ==========
# 📊 GERAL
# ==========
print("\n📊 === ESTATÍSTICAS GERAIS ===")
print("Média geral:\n", df.mean(numeric_only=True))
print("\nMediana geral:\n", df.median(numeric_only=True))
print("\nModa geral:\n", df.mode(numeric_only=True))
print("\nDesvio padrão geral:\n", df.std(numeric_only=True))
print("\nCovariância geral:\n", df.cov(numeric_only=True))
print("\nCorrelação geral:\n", df.corr(numeric_only=True))

Q1 = df.quantile(0.25, numeric_only=True)
Q3 = df.quantile(0.75, numeric_only=True)
print("\nIQR geral:\n", Q3 - Q1)

# ==========
# 📊 POR ESPÉCIE
# ==========
print("\n📊 === ESTATÍSTICAS POR ESPÉCIE ===")

for especie in df["species"].unique():
    print(f"\n🔸 Espécie: {especie.upper()}")
    df_esp = df[df["species"] == especie]

    print("Média:\n", df_esp.mean(numeric_only=True))
    print("Mediana:\n", df_esp.median(numeric_only=True))
    print("Moda:\n", df_esp.mode(numeric_only=True).iloc[0])
    print("Desvio padrão:\n", df_esp.std(numeric_only=True))

    Q1 = df_esp.quantile(0.25, numeric_only=True)
    Q3 = df_esp.quantile(0.75, numeric_only=True)
    print("IQR:\n", Q3 - Q1)

    print("Covariância:\n", df_esp.cov(numeric_only=True))
    print("Correlação:\n", df_esp.corr(numeric_only=True))

# ==========
# ⚖️ Normalização e Padronização (Geral)
# ==========
print("\n⚖️ Normalização (0 a 1):")
scaler_minmax = MinMaxScaler()
df_norm = pd.DataFrame(
    scaler_minmax.fit_transform(df.select_dtypes(include="number")),
    columns=df.select_dtypes(include="number").columns
)
print(df_norm.head())

print("\n⚖️ Padronização (Z-score):")
scaler_std = StandardScaler()
df_std = pd.DataFrame(
    scaler_std.fit_transform(df.select_dtypes(include="number")),
    columns=df.select_dtypes(include="number").columns
)
print(df_std.head())



# Questões
'''
1. Qual espécie possui, em média, a menor largura de pétala?
2. Existe correlação entre o comprimento da pétala e o comprimento da sépala?
3. Qual das variáveis numéricas possui maior variabilidade?
4. Qual espécie é mais homogênea em termos de medidas (menor desvio padrão)?
5. Quais variáveis seriam mais úteis para diferenciar as espécies?
6. Existe alguma espécie cujas pétalas e sépalas não têm correlação significativa?
7. Qual o intervalo interquartil (IQR) da largura da sépala da Virginica? Ele é maior ou menor que o da Setosa?
8. Após padronizar os dados (z-score), qual variável ainda mostra maior variação?
9. A largura da sépala é um bom indicador para diferenciar espécies?
10. Existe alguma variável com distribuição próxima da normal?
'''