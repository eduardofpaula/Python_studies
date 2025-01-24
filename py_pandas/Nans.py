# %%
import pandas as pd
import numpy as np

# %%

data = {
    'nome': ['Téo', 'Nah', 'Lah', 'Mah', 'Jo'],
    'idade': [31, 32, 34, 12, np.nan],
    'renda': [np.nan, 3245, 357, 12432, np.nan],
}

df = pd.DataFrame(data)
df

# %%

# isna() retorna se o valor da coluna é Nan ou não, se for, o valor é True
# sum() retorna a soma dos valores nan
df['idade'].isna().sum()

# %%

# ele vai em cada célula e verifica se é nan
# sum ta somando a linha inteira e da pra saber se tem nan ou não
df.isna().sum()
# %%

# para a media, ele considera que True é 1 e False é 0
df.isna().mean()
# %%

# fillna() serve para preencher os locais com dados faltantes
# aqui os dados faltantes estão sendo preenchidos com a média de cada um dos valores de idade e renda
df.fillna({'idade': df['idade'].mean(), 'renda': df['renda'].mean()})
# %%

# remove a linha inteira se tiver um valor com Nan, all só remove se todas as linhas for Nan, any remove a linha inteira se pelo menos 1 das linhas tiverem Nan
df.dropna(subset=['idade', 'renda'], how='all')

# %%

# axis considera a coluna ao inves da linha
# tresh considera como requisito para dropar valores não-nulos
df.dropna(axis=1, thresh=4)
