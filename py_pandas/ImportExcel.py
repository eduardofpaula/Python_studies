# %%
import pandas as pd

# %%

df = pd.read_excel('../data/transactions.xlsx')
df

# %%

# retorna o tamanho de linhas e colunas em forma de tupla
df.shape

# %%

# retorna as 5 primeiras linahs dataframe
df.head()

# %%

# retorna as ultimas 5 linhas do dataframe
df.tail()

# %%

colunas = ['UUID', 'Points', 'IdCustomer', 'DtTransaction']
df = df[colunas]
df

# %%

df.info(memory_usage='deep')
