'''
1. Qual tipo de vinho tem a maior média de teor alcoólico?

2. Existe correlação entre o teor de álcool e a cor do vinho?

3. Qual variável possui maior desvio padrão dentro de cada tipo de vinho?

4. Há alguma variável com valores extremos? Use IQR para detectar.

5. Qual tipo de vinho apresenta maior variabilidade geral?

6. Existe alguma variável fortemente correlacionada com a intensidade da cor?

7. Qual o tipo de vinho com maior concentração média de flavonoides?

8. Há correlação negativa entre alguma dupla de variáveis?

9. Após padronizar os dados, qual variável ainda apresenta grande variabilidade relativa?

10. Se você tivesse que escolher 2 variáveis para prever o tipo do vinho, quais seriam e por quê?
'''
from sklearn.datasets import load_wine
import pandas as pd

wine = load_wine(as_frame=True)
df = wine.frame
df.rename(columns={"target": "wine_type"}, inplace=True)
df["wine_type"] = df["wine_type"].map(dict(enumerate(wine.target_names)))

print(df.head())