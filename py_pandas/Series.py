# %%
import pandas as pd

idades = [30, 42, 90, 34]

series_idades = pd.Series(idades)
print(series_idades)

# %%

# media
print(series_idades.mean())

# variancia
print(series_idades.var())

# mediana
print(series_idades.median())

# quartil
print(series_idades.quantile(0.75))

# desvio padrao
print(series_idades.std())

# describe, retorna diversas estatisticas
print(series_idades.describe())

# %%

# shape retorna o tamanho da série
series_idades.shape

# %%
# acessando elementos pelo indice
series_idades[2]

# %%

# informacoes sobre o indice da serie
series_idades.index

# %%

# alterando o indice da serie
print(series_idades)
series_idades.index = ["e", "d", "c", "a"]
print(series_idades["e"])

# %%

# acessando elementos pelo indices explicitamente, ignorando o indices da serie
series_idades.iloc[2]

# %%

# acessando elementos da serie pelo indice implicito com inicio e fim
series_idades.iloc[2:4]

# %%
# loc garante que esta pegando pelo indice explicito
# iloc garante que esta pegando pela posicao

# acessando elementos pelo indices explicitamente, considerando o indices da série
series_idades.loc["e"]

# %%

# pode atribuir um nome a serie
series_idades.name = "idades"
print(series_idades)
