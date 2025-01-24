# %%
import pandas as pd

# %%

df = pd.read_csv('../data/customers.csv', sep=';')
df

# %%

# ordenando pelos pontos, e ja sobscreve o proprio objeto df, ascending serve para denominar a ordem, pode ser crescente(default) ou decrescente
df.sort_values(by='Points', ascending=False, inplace=True)
# renomeando colunas
df.rename(
    columns={'UUID': 'Id', 'Name': 'Nome', 'Points': 'Pontos'}, inplace=True
)
df

# %%

# primeiro ordena pelos pontos de forma decrescente, e depois pelo Name de forma crescente
df = df.sort_values(by=['Points', 'Name'], ascending=[False, True])
df

# %%

# maneira correta e indicada para se fazer uma pipeline de dados
df = df.sort_values(by='Points', ascending=False).rename(
    columns={'UUID': 'Id', 'Name': 'Nome', 'Points': 'Pontos'}
)
df
