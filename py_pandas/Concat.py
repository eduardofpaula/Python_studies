# %%

import pandas as pd

data_01 = {
    'id': [1, 2, 3, 4],
    'nome': ['Teo', 'Mat', 'Nah', 'Mah'],
    'idade': [31, 31, 32, 32],
}

df_01 = pd.DataFrame(data_01)
df_01

# %%

data_02 = {
    'id': [5, 6, 7, 8],
    'nome': ['Jose', 'Nathan', 'Arnaldo', 'Mario'],
    'idade': [23, 33, 19, 21],
}

df_02 = pd.DataFrame(data_02)
df_02

# %%

# Concatenando os dataframes, o drop=True serve para resetar o index e descartar o index do dataframe original
pd.concat([df_01, df_02]).reset_index(drop=True)


# %%
data_03 = {
    'sobrenome': ['Calvo', 'Silva', 'Costa', 'Souza'],
    'renda': [3100, 3100, 3200, 3200],
}

df_03 = pd.DataFrame(data_03)
df_03
# %%

# concatenando os dataframes com axis=1, ou seja, concatenando as colunas de maneira horizontal
concat_horizontal = pd.concat([df_01, df_03], axis=1)
concat_horizontal
