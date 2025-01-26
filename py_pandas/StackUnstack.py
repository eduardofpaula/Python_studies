# %%

import pandas as pd

df = pd.read_csv('../data/edu_consolidado.csv', sep=';')
df

# %%
df = df.set_index(['cod', 'nome', 'período'])
df
# %%

# .stack() empilha as colunas do dataframe para o índice (ou seja, transforma as colunas em linhas)
df_stack = (
    df.stack()
    .reset_index()
    .rename(
        columns={
            'cod': 'Código',
            'nome': 'Nome',
            'período': 'Período',
            'level_3': 'Tipo Homicidio',
            0: 'Qtde',
        }
    )
)

df_stack

#%%

# unsetack() faz o contrário do stack(), ou seja, transforma as linhas em colunas
df_unstack = (
    df_stack.set_index(['Código', 'Nome', 'Período', 'Tipo Homicidio'])
    .unstack()
    .reset_index()
)

# %%

homicidios = df_unstack['Qtde'].columns.tolist()
indentificadores = df_unstack.columns.droplevel(1).tolist()[:3]

df_unstack.columns = indentificadores + homicidios
df_unstack

# %%

# ! stack e unstack são métodos usados para reorganizar os níveis de um DataFrame ou Series

# stack
# Objetivo: Transforma colunas em índices.
# Como funciona: Empilha os dados, movendo os valores das colunas para a estrutura de índice hierárquico.
# Usado em: Converter um DataFrame largo em um formato mais longo.

df = pd.DataFrame(
    {'A': [1, 2], 'B': [3, 4], 'C': [5, 6]}, index=['linha1', 'linha2']
)

print('Original:')
print(df)

# Aplicando stack
stacked = df.stack()
print('\nApós stack:')
print(stacked)
# %%

# unstack
# Objetivo: Transforma índices em colunas.
# Como funciona: Desempilha os níveis mais internos de um índice hierárquico, movendo-os de volta para colunas.
# Usado em: Converter uma estrutura longa em um formato mais largo.

# Aplicando unstack
unstacked = stacked.unstack()
print('\nApós unstack:')
print(unstacked)
