# %%
import pandas as pd

# %%

data = {
    'Nome': ['Téo', 'Nah', 'Maria', 'Nah', 'Lara', 'Téo'],
    'Idade': [32, 33, 2, 33, 31, 32],
    'updated_at': [1, 2, 3, 1, 2, 3],
}

df = pd.DataFrame(data)
df

# %%

# remover as duplicata da forma simples
df = df.drop_duplicates()
df

# %%

# recomenda-se primeiro ordenar os valores para depois fazer a remoção de duplicatas
df.sort_values(by='updated_at', ascending=True)

# %%

# remover duplicatas de mais de uma coluna igual, keep first preserva a primeira linha, keep last preserva a linha mais antiga
df.drop_duplicates(subset=['Nome', 'Idade'], keep='last')
