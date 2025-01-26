# %%
import pandas as pd
import numpy as np
import dateutil as dt

df = pd.read_excel('../data/transacao_cartao.xlsx')
df

# %%

# transformando a coluna dtTransaction em datetime, formatação de data dd/mm/yyyy
df['dtTransaction'] = pd.to_datetime(df['dtTransaction'], format='%Y-%m-%d')

df
# %%

# criar uma lista com o valor da parcela, recebendo a linha como parâmetro e dividindo o valor pelo número de parcelas
def fatia_parcelas(row):
    return [row['Valor'] / row['Parcelas'] for i in range(row['Parcelas'])]


# aplicar a função fatia_parcelas em cada linha do dataframe
df['ValorParcela'] = df.apply(fatia_parcelas, axis=1)

df

# %%

# explode a coluna ValorParcela, criando uma linha para cada valor da lista
df_fatura = df.explode('ValorParcela')
df_fatura

# %%

# limpando as colunas que não serão mais utilizadas
df_fatura = df_fatura.drop(['Valor', 'Parcelas'], axis=1)

df_fatura

# %%

# criar uma coluna com o número de meses a serem adicionados à data da transação para auxiliar na criação da fatura
# rank('first') cria um ranking para cada idTransaction, começando em 1
df_fatura['Months_add'] = (
    df_fatura.groupby('idTransaction')['dtTransaction']
    .rank('first')
    .astype(int)
)

df_fatura
# %%

# criar uma função que adiciona os meses à data da transação
def add_months(row):
    new_date = row['dtTransaction'] + np.timedelta64(row['Months_add'], 'm')
    dt_str = new_date.strftime('%Y-%M-15')
    return dt_str


# aplicar a função add_months em cada linha do dataframe, criando a coluna DtFatura
df_fatura['DtFatura'] = df_fatura.apply(add_months, axis=1)
df_fatura
# %%

# agrupar por idCliente e DtFatura, somando os valores das parcelas
df_fatura_mes = (
    df_fatura.groupby(['idCliente', 'DtFatura'])['ValorParcela']
    .sum()
    .reset_index()
)
df_fatura_mes
# %%

# pivotar a tabela para que cada mês seja uma coluna e cada linha seja um cliente
# preencher os valores nulos com 0
# pivot table serve para transformar os valores de uma coluna em colunas
df_fatura_mes = (
    df_fatura_mes.pivot_table(
        columns='DtFatura', index='idCliente', values='ValorParcela'
    )
    .fillna(0)
    .reset_index()
)

# %%
# salvar o dataframe em um arquivo excel
df_fatura_mes.to_excel('Fatura_detalhada.xlsx')
