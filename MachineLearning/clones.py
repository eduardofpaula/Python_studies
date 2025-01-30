# %%
import pandas as pd

df = pd.read_parquet('../MachineLearning/data/dados_clones.parquet')
df
# %%

# analise simples calculando a média emtre clones aptos e defeituosos medindo estatura e massa, não parece significativo
df.groupby(['Status '])[['Estatura(cm)', 'Massa(em kilos)']].mean()
# %%
# definindo meu target como um booleano para facilitar a análise, 1 para apto e 0 para defeituoso
df['Status_bool'] = df['Status '] == 'Apto'
df

# %%

# média de clones aptos e defeituosos medindo a distância entre ombros
df.groupby(['Distância Ombro a ombro'])['Status_bool'].mean()
# %%
# média de clones aptos e defeituosos medindo o tamanho do crânio
df.groupby(['Tamanho do crânio'])['Status_bool'].mean()

# %%
# média de clones aptos e defeituosos medindo o tamanho dos pés
df.groupby(['Tamanho dos pés'])['Status_bool'].mean()

# %%
# média de clones aptos e defeituosos medindo pelo General Jedi encarregado
# mostra que os clones shaak ti e yoda estão cagados
df.groupby(['General Jedi encarregado'])['Status_bool'].mean()

# %%

features = [
    'Estatura(cm)',
    'Massa(em kilos)',
    'Distância Ombro a ombro',
    'Tamanho do crânio',
    'Tamanho dos pés',
]

# variaveis categoricas
cat_features = [
    'Distância Ombro a ombro',
    'Tamanho do crânio',
    'Tamanho dos pés',
]

X = df[features]

# %%

# Transformação de categorias para Numérico
from feature_engine import encoding

# onehot encoding serve para transformar variáveis categóricas em numéricas
# para cada categoria ele cria uma coluna e atribui 1 ou 0 se a categoria está presente ou não, respectivamente
onehot = encoding.OneHotEncoder(variables=cat_features)
onehot.fit(X)
X = onehot.transform(X)
X


# %%
from sklearn import tree

# criando a árvore de decisão
arvore = tree.DecisionTreeClassifier(max_depth=4)
arvore.fit(X, df['Status '])
# %%
import matplotlib.pyplot as plt

plt.figure(dpi=600)

# plotando a árvore
tree.plot_tree(
    arvore, class_names=arvore.classes_, feature_names=X.columns, filled=True
)
