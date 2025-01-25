# %%
import pandas as pd

# %%
# * Agregações é uma forma de resumir o meu conjunto de dados por meio de alguma estatistica de resumo

df = pd.read_excel('../data/transactions.xlsx')
df

# %%

# filtrando o dataset inteiro para um usuario em especifico e somando todos os pontos dele
condicao = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df_user = df[condicao]
df_user['Points'].sum()

# %%

# fazendo o loop manual para calcular a soma de pontos de todos os usuarios
# forma ruim de fazer
pontos = {}
for i in df['IdCustomer'].unique():
    condicao = df['IdCustomer'] == i
    pontos[i] = df[condicao]['Points'].sum()

pontos

# %%

# agrupando elementos pelo idcustomer, somando todos os pontos e tirando a soma deles de forma vetorial
df_sumary = df.groupby(['IdCustomer'])['Points'].sum()
# reset index transforma em dataframe com os itens ordenados
df_sumary.reset_index()

# %%

(
    df.groupby(['IdCustomer'])
    .agg({'Points': 'sum', 'UUID': 'count', 'DtTransaction': 'max'})
    .rename(
        columns={
            'Points': 'Valor',
            'UUID': 'Frequencia',
            'DtTransaction': 'Ultima Compra',
        }
    )
    .reset_index()
)
# %%
# importando a lib para trabalhar com datas
import datetime

# aqui mostra como a logica das datas ta funcionando
# primeiro elemento do campo data, que retorna um timestamp
data1 = df['DtTransaction'][0]
# pegando a data atual
now = datetime.datetime.now()

# subtraindo a data atual pela data exemplo e pegando os dias
(now - data1).days

# %%

# criando uma função para calcular a recencia
def recencia(x):
    # pegando a data mais recente e subtraindo pela data atual
    diff = datetime.datetime.now() - x.max()
    # pegando os dias
    return diff.days


(
    df.groupby(['IdCustomer'])
    .agg(
        {
            'Points': 'sum',
            'UUID': 'count',
            # aplicando a função recencia
            'DtTransaction': recencia,
        }
    )
    .rename(
        columns={
            'Points': 'Valor',
            'UUID': 'Frequencia',
            'DtTransaction': 'Recencia',
        }
    )
    .reset_index()
)
