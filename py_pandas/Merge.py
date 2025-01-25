# %%

import pandas as pd

data_users = {
    'id': [1, 2, 3, 4],
    'nome': ['Teo', 'Mat', 'Nah', 'Mah'],
    'idade': [31, 31, 32, 32],
}

df_user = pd.DataFrame(data_users)
df_user

# %%

data_transacoes = {
    'id_user': [1, 1, 1, 2, 3, 3, 5],
    'vl': [432, 532, 123, 6, 4, 87, 10],
    'qtProdutos': [2, 1, 3, 6, 10, 2, 7],
}

df_transacao = pd.DataFrame(data_transacoes)
df_transacao
# %%

# SELECT *
# FROM df_transacao
# LEFT JOIN df_user
# ON df_transacao.id_user = df_user.id

# merge é o join do pandas
df_transacao.merge(
    df_user,
    # mantem todas as linhas do df_transacao
    how='left',
    left_on='id_user',
    right_on='id',
)

# %%

# SELECT *
# FROM df_transacao
# INNER JOIN df_user
# ON df_transacao.id_user = df_user.id

df_transacao.merge(
    df_user,
    # how é o tipo de join
    how='inner',
    left_on=['id_user'],
    right_on=['id'],
)

# %%

# ! Como funciona os diferentes tipos de join

# ? Inner Join: Retorna apenas as linhas onde há correspondência em ambos os DataFrames.

# ? Left Join: Retorna todas as linhas do DataFrame da esquerda e as linhas correspondentes do DataFrame da direita. Se não houver correspondência, os valores do DataFrame da direita serão NaN.

# ? Right Join: Retorna todas as linhas do DataFrame da direita e as linhas correspondentes do DataFrame da esquerda. Se não houver correspondência, os valores do DataFrame da esquerda serão NaN.

# ? Outer Join: Retorna todas as linhas quando há correspondência em um dos DataFrames. As áreas sem correspondência serão preenchidas com NaN.

df1 = pd.DataFrame(
    {
        'A': ['A0', 'A1', 'A2', 'A3'],
        'B': ['B0', 'B1', 'B2', 'B3'],
        'key': ['K0', 'K1', 'K2', 'K3'],
    }
)

df2 = pd.DataFrame(
    {
        'C': ['C0', 'C1', 'C2', 'C3'],
        'D': ['D0', 'D1', 'D2', 'D3'],
        'key': ['K0', 'K1', 'K2', 'K4'],
    }
)

# %%
# Inner Join
inner_join = pd.merge(df1, df2, on='key', how='inner')
print('Inner Join:\n', inner_join)
# %%
# Left Join
left_join = pd.merge(df1, df2, on='key', how='left')
print('Left Join:\n', left_join)
# %%
# Right Join
right_join = pd.merge(df1, df2, on='key', how='right')
print('Right Join:\n', right_join)
# %%
# Outer Join
outer_join = pd.merge(df1, df2, on='key', how='outer')
print('Outer Join:\n', outer_join)
