# %%
import pandas as pd

# %%

# lendo e extraindo o arquivo csv
df = pd.read_csv('../../data/ipea/homicidios.csv', sep=';')
df

# %%

# transformando em string e pegando o primeiro elemento
linha = str(df.shape[0])
print(f'Quantidade de Linhas do meu Dataframe: {linha}')

colunas = str(df.shape[1])
print(f'Quantidade de Colunas do meu Dataframe: {colunas}')
# %%

coluna1 = df.columns[0]
print(f'Nome da primeira coluna: {coluna1}')

coluna2 = df.columns[-1]
print(f'Nome da última coluna: {coluna2}')
