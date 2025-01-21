# %%
import pandas as pd

# %%

dados = {'nome': ['Téo', 'Nah', 'Napoleão'], 'idade': [31, 32, 14]}
dfDados = pd.DataFrame(dados)
dfDados

# %%

# sumario de cada coluna
dfDados['nome'].describe()

# %%

# definindo a variavel como o describe do dataframe
mediaIdade = dfDados.describe()
# média da coluna idade
print(f"Média Idade: {round(mediaIdade['idade']['mean'],2)}")
# ultimo elemento da coluna nome
print(f"Último nome: {dfDados['nome'][2]}")
