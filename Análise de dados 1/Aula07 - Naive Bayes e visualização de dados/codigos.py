import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Distribuição de inadimplência
sns.countplot(x=baseCredito['default'])
plt.title('Distribuição de Pagamentos')

# Histograma da idade (já tratada)
plt.hist(baseCredito['age'])
plt.title('Distribuição da Idade')

# Scatter Matrix
grafico = px.scatter_matrix(baseCredito, dimensions=['income', 'loan', 'age'], color='default')
grafico.show()
