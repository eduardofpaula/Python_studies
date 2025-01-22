# %%
import pandas as pd

dfChat = pd.read_csv(
    '../data/products.csv',
    sep=';',
    #  header=None,
    names=['id', 'Name', 'Description'],
)
dfChat

# %%

# outra forma de renomear colunas sem o inplace
dfChat = dfChat.rename(columns={'Name': 'Nome', 'Description': 'Descrição'})
dfChat

# %%

# o inplace ja altera o proprio objeto automaticamente
dfChat.rename(
    columns={'Name': 'Nome', 'Description': 'Descrição'}, inplace=True
)
dfChat
