# %%
import numpy as np

dados = [1, 3, 4, 6, 7, 8, 10, 12, 14, 15]

q1 = np.percentile(dados, 25)
q2 = np.percentile(dados, 50)
q3 = np.percentile(dados, 75)

print(f'Q1: {q1}, Q2: {q2}, Q3: {q3}')

# %%

dados = [4, 8, 12, 16]

q1 = np.percentile(dados, 25)
q2 = np.percentile(dados, 50)

print(f'Q1: {q1}, Q2: {q2}')
