#  %%
import pandas as pd

# %%

# le o arquivo csv e atruibui a uma variavel
df_customers = pd.read_csv('../data/customers.csv', sep=';')
df_customers

# %%

# retorna uma tupla com numero de linhas e colunas
df_customers.shape

# %%

# retorna as informações do dataframe com o tamanho em memória correto
df_customers.info(memory_usage='deep')

# %%

# retorna as estatisticas da coluna points
df_customers['Points'].describe()

# %%

# condicional que retorna uma series boleana com todos valores points maiores que 1000
condicao = df_customers['Points'] > 1000
# retorna somente linhas true de acordo com a condição
df_customers[condicao]

# %%

# atribui o valor maximo da coluna points, faz uma condicional com a tabela points para encontrar o maior valor e compara com o dataframe
maximo = df_customers['Points'].max()
condicao = df_customers['Points'] == maximo
df_customers[condicao]

# %%

# outra forma de encontrar o maior elemento atraves de uma pesquisa condicional no dataframe
condicao = df_customers['Points'] == df_customers['Points'].max()
df_customers[condicao]

# %%

# outra forma de encontrar o maior elemento através de uma pesquisa condicional no dataframe
df_customers[df_customers['Points'] == df_customers['Points'].max()]

# %%

# faz a condição para encontrar o maior valor
condicao = df_customers['Points'] == df_customers['Points'].max()
# atribui a uma variavel com o dataframe
maior = df_customers[condicao]
# encontra o nome na coluna name do maior valor encontrado no dataframe
maior['Name'].iloc[0]

# %%

# condicional para fazer pesquisa vetorial no dataframe
condicao = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
df_customers[condicao]

# %%

# se for primeiro aplciar um filtro pra depois manipular um dado, faça uma copia, pois é perigoso, pode estar alterando o dataframe principal
condicao = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
df_1000_2000 = df_customers[condicao].copy()

df_1000_2000['Points'] = df_1000_2000['Points'] + 1000
df_1000_2000

# %%

# ordenar as colunas, primeiro joga para uma lista
colunas = df_customers.columns.to_list()
# ordena a lista
colunas.sort()

# reatribuiu ao dataframe principal, agora o dataframe original esta com as colunas ordenadas
df_customers = df_customers[colunas]
df_customers

# %%

# renomear colunas do dataframe
df_customers = df_customers.rename(
    columns={'Name': 'Nome', 'Points': 'Pontos'}
)
df_customers

# %%

# renomear colunas do dataframe sem precisar reatribuir o valor
df_customers.rename(columns={'UUID': 'Id'}, inplace=True)
df_customers
