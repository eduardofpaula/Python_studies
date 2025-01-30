# %%
import pandas as pd

df = pd.read_excel('../MachineLearning/data/dados_cerveja.xlsx')
df

# %%

# no sklearn, temos que transformar os dados em numeros
# variaveis, atributos, covariaveis, variaveis explicativas, preditivas, independentes

# filtros
# filtro_temp = df['temperatura'] == 1
# filtro_copo = df['copo'] == 1
# filtro_espuma = df['espuma'] == 1
# filtro_cor = df['cor'] == 1 

features = ['temperatura','copo','espuma','cor']
target = 'classe'

x = df[features]
y = df[target]

# %%

# tem que alterar os dados senão a lib não reconhece
x = x.replace({'mud':1,
               'pint':0,
               'sim':1,
               'não':0,
               'escura': 1,
               'clara':0})
x


# %%
from sklearn import tree

arvore = tree.DecisionTreeClassifier(random_state=42)
arvore.fit(x,y)
# %%
import matplotlib.pyplot as plt

plt.figure(dpi=600)

tree.plot_tree(arvore,
               class_names=arvore.classes_,
               feature_names=features,
               filled=True)

# %%


probas = arvore.predict_proba([[-5,1,0,1]])[0]
pd.Series(probas, index=arvore.classes_)