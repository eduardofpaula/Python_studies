# %%
import pandas as pd

# %%

"""dicionario com listas de dados"""
data = {
    "nome": ["João", "Maria", "José", "Pedro", "Ana", "Paula", "Carlos", "Lucas"],
    "idade": [30, 42, 90, 34, 50, 60, 70, 80],
    "cidade": [
        "São Paulo",
        "Rio de Janeiro",
        "Curitiba",
        "Porto Alegre",
        "Salvador",
        "Recife",
        "Fortaleza",
        "Manaus",
    ],
}

data["idade"][0]

# %%
# Criando um DataFrame
df = pd.DataFrame(data)
df

# %%
# retornando o tipo de dado
type(df["idade"])

# %%
# pegando o primeiro elemento do DataFrame com o método iloc
df["idade"].iloc[0]

# %%
# pegando o primeiro elemento do DataFrame com o método loc
df["cidade"]

# %%
# pegando os primeiros elementos do Dataframe com o método loc, retornando uma series
df.iloc[0]

# diferenças entre loc e iloc
# loc -> retorna o valor do índice
# iloc -> retorna o valor da posição

# %%

# retorna o tamanho do DataFrame
df.index

# %%

# retorna as colunas do DataFrame
df.columns

# %%

# retorna as informações do DataFrame
df.info(memory_usage="deep")

# %%

# retorna as estatísticas do DataFrame
df.dtypes

# %%

# atribuir uma coluna nova
df["peso"] = [90, 70, 80, 100]

sumario = df.describe()

sumario["peso"]["mean"]

# %%

# retorna as duas primeiras linhas do DataFrame
df.head(2)

# %%

# retorna as duas últimas linhas do DataFrame
df.tail(2)
