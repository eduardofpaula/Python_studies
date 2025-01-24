# %%
import pandas as pd

# %%

df = pd.read_csv('../data/customers.csv', sep=';')
df
# %%
# mostrar as informações
df.info()
# mostrar as colunas com seus tipos
df.dtypes

# %%

# convertendo tipo da coluna de inteiro para string
df = df['Points'].astype(str)

# %%
# criando uma nova coluna que multiplica points por 2
df['Points_double'] = df['Points'] * 2
# %%
# convertendo o tipo de duas colunas ao mesmo tempo
df[['Points_double', 'Points']].astype(float)
# %%
# não é possivel transformar de string para inteiro ou float, DA ERRO
df[['Name']].astype(int)
# %%

# criando uma nova coluna, não sendo uma string ou int ou float, ele determina como object
df['Lista'] = [[1, 2] for i in df.index]
df

# %%
df.dtypes
