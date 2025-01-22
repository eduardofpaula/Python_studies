# %%

import pandas as pd

# %%

# lendo e atribuindo o arquivo csv a uma variavel transformando-o em dataframe
df = pd.read_csv('../../data/ipea/homicidios-mulheres-negras.csv', sep=';')
df

# %%

# colunas do tipo int
colunas_int = df.select_dtypes(include=['int64']).columns
colunas_int = list(colunas_int)
print(f'Colunas do tipo numérico: {colunas_int}')

# colunas do tipo object
colunas_obj = df.select_dtypes(include='object').columns
colunas_obj = list(colunas_obj)
print(f'Colunas do tipo object: {colunas_obj}')

# tamanho dos dados em memoria
tamanho_dados = df.memory_usage(deep=True).sum()
print(f'Tamanho do DataFrame em memoria: {tamanho_dados} bytes')
