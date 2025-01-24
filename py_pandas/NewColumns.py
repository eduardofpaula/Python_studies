# %%
import pandas as pd
import numpy as np

# %%

df = pd.read_csv('../data/customers.csv', sep=';')
df

# %%

# adicionando uma coluna nova que multiplica a coluna pontos por 2
df['Points_double'] = df['Points'] * 2
df

# %%
# adicionando uma coluna nova que divide a points double pela points
df['Points_ratio'] = df['Points_double'] / df['Points']
df
# %%

# adicionando uma nova coluna de logaritmos utilizando a biblioteca numpy
df['Points_log'] = np.log(df['Points'])
df

# modificando todas as strings da coluna name para maiusculo com um loop, FORMA RUIM DE FAZER essa conversão
upperCase = []
for i in df['Name']:
    upperCase.append(i.upper())
df['Name_upper'] = upperCase
df

# %%
# definindo uma função determinando oque fazer com o elemento recebido, nesse caso, é cada linha da coluna 'Name'
def get_first(nome: str):
    nome = nome.upper()
    return nome.split('_')[0]


# %%

# apply ajuda a aplicar algo a cada elemento da coluna, nesse caso foi chamada uma função
df['Name'] = df['Name'].apply(get_first)
df

# %%

# definindo uma função lambda, lambda é uma função simples
# split('_') separa a string em duas partes, antes e depois do '_', o [0] pega a primeira parte
df['Name'] = df['Name'].apply(lambda x: x.upper().split('_')[0])
df

# %%

# função para retornar uma string de acordo com a quantidade de pontos
def intervaloPontos(pontos: int):
    if pontos < 2500:
        return 'Baixo'
    if pontos < 3500:
        return 'Médio'
    else:
        return 'Alto'


df['Pontuacao'] = df['Points'].apply(intervaloPontos)
df

# %%

# função em lambda que transforma a string em upper e remove o traço
df['UUID'] = df['UUID'].apply(lambda x: x.upper().replace('-', ''))
df
# %%

data = {
    'nome': ['Teo', 'Nah', 'Maria', 'Lara'],
    'recencia': [1, 30, 10, 45],
    'valor': [100, 2000, 15, 500],
    'frequencia': [2, 5, 1, 15],
}

dados = pd.DataFrame(data)

# %%


def rfv(row):

    nota = 0

    if row['recencia'] <= 10:
        nota += 10
    elif 10 < row['recencia'] <= 30:
        nota += 5
    elif row['recencia'] > 30:
        nota += 0

    if row['valor'] > 1000:
        nota += 10
    elif 100 <= row['valor'] < 1000:
        nota += 5
    elif row['valor'] < 100:
        nota += 0

    if row['frequencia'] > 10:
        nota += 10
    elif 5 <= row['frequencia'] < 10:
        nota += 5
    elif row['frequencia'] < 5:
        nota += 0

    return nota


# %%

dados['RFV'] = dados.apply(rfv, axis=1)
dados
