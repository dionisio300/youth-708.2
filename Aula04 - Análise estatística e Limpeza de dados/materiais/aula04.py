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

print("✅ Dataset carregado com sucesso!")
print(df.head())

# ============================
# 📊 ESTATÍSTICAS DESCRITIVAS
# ============================
print("\n🔢 Estatísticas descritivas:")
print(df.describe())

# Média
print("\n📌 Média:")
print(df.mean(numeric_only=True))

# Mediana
print("\n📌 Mediana:")
print(df.median(numeric_only=True))

# Moda
print("\n📌 Moda:")
print(df.mode(numeric_only=True))

# Mínimo e Máximo
print("\n📌 Mínimo:")
print(df.min(numeric_only=True))
print("\n📌 Máximo:")
print(df.max(numeric_only=True))

# ============================
# 📈 VARIABILIDADE
# ============================
# Variância
print("\n📈 Variância:")
print(df.var(numeric_only=True))

# Desvio padrão
print("\n📈 Desvio padrão:")
print(df.std(numeric_only=True))

# Quartis e IQR
print("\n📈 Quartis e IQR:")
Q1 = df.quantile(0.25, numeric_only=True)
Q2 = df.quantile(0.50, numeric_only=True)
Q3 = df.quantile(0.75, numeric_only=True)
IQR = Q3 - Q1
print(f"Q1:\n{Q1}\n")
print(f"Q2 (Mediana):\n{Q2}\n")
print(f"Q3:\n{Q3}\n")
print(f"IQR (Q3 - Q1):\n{IQR}")

# ============================
# 🔄 RELACIONAMENTO ENTRE VARIÁVEIS
# ============================
# Covariância
print("\n🔄 Covariância:")
print(df.cov(numeric_only=True))

# Correlação
print("\n🔄 Correlação:")
print(df.corr(numeric_only=True))

# ============================
# ⚖️ NORMALIZAÇÃO E PADRONIZAÇÃO
# ============================
print("\n⚖️ Normalização (0 a 1):")
scaler_minmax = MinMaxScaler()
dados_norm = scaler_minmax.fit_transform(df.select_dtypes(include="number"))
df_norm = pd.DataFrame(dados_norm, columns=df.select_dtypes(include="number").columns)
print(df_norm.head())

print("\n⚖️ Padronização (Z-score):")
scaler_std = StandardScaler()
dados_std = scaler_std.fit_transform(df.select_dtypes(include="number"))
df_std = pd.DataFrame(dados_std, columns=df.select_dtypes(include="number").columns)
print(df_std.head())
