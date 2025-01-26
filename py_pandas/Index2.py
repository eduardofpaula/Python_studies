# %%
import pandas as pd
import os

# função para importar os arquivos csv
def import_etl(path: str):

    # pegando o nome do arquivo
    name = path.split('/')[-1].split('.')[0]

    # lendo o arquivo csv
    df = (
        pd.read_csv(path, sep=';')
        .rename(columns={'valor': name})
        .set_index(['cod', 'nome', 'período'])
    )

    # retornando o dataframe
    return df


# %%

# pegando os arquivos do diretorio
path = '../data/ipea/'
# pegando os arquivos do diretorio
files = os.listdir(path)

# loop para importar os arquivos
dfs = []
for i in files:
    dfs.append(import_etl(path + i))

# concatenando os dataframes
df_edu = pd.concat(dfs, axis=1).reset_index()
# salvando o arquivo csv
df_edu.to_csv('../data/bia_consolidado.csv', sep=';', index=False)
