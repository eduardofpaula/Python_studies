# %%
import pandas as pd

# %%

df = pd.read_excel('../../data/transactions.xlsx')
df

# %%

# ordenando por ordem descrescente
# preservando o primeiro valor de cada duplicata
df_last = df.sort_values('DtTransaction', ascending=False).drop_duplicates(
    subset=['IdCustomer'], keep='first'
)

# retorna o tamanho de linhas com valores unicos
df_last['IdCustomer'].nunique()

# %%

# condição comparando com o dataframe original para ver qual o ultimo elemento
condicao = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df[condicao]

# %%

# pesquisando o id que sobrou depois da remoção de duplicata para conferir
df_last[df_last['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3']
