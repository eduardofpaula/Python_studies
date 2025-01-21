# %%
import pandas as pd

# %%

# atribuindo uma variavel para ser o conjunto de dados
dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
# ordenando o conjunto de dados
dados.sort()

# %%

# transformando o conjunto de dados em uma series para ser mais facil de trabalhar junto ao pandas
series_dados = pd.Series(dados)

# %%

# Média
print(f"Média: {round(series_dados.mean(),2)}")

# Desvio padrão
print(f"Desvio Padrão: {round(series_dados.std(),2)}")

# Valor Maximo
print(f"Valor Maximo: {series_dados.max()}")
