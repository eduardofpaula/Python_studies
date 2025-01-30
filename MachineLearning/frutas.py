# %%
import pandas as pd

df = pd.read_excel('../MachineLearning/data/dados_frutas.xlsx')
df

# %%

filtro_redonda = df['Arredondada'] == 1
filtro_suculenta = df['Suculenta'] == 1
filtro_vermelha = df['Vermelha'] == 1
filtro_doce = df['Doce'] == 1

# os filtros ajudam a encontrar a resposta correta 
df[filtro_redonda & filtro_suculenta & filtro_vermelha & filtro_doce]
# %%
from sklearn import tree

# definir uma lista de atributos
features = ['Arredondada','Suculenta','Vermelha','Doce']
# definir target, quem eu quero prever, quem eu quero que a maquina aprenda oque é oque?
target = 'Fruta'

x = df[features]
y = df[target]

# %%

# definindo objeto, metodo fit é dizendo para minha maquina, APRENDA!! 
# fit constroi minha arvore de decisão
arvore = tree.DecisionTreeClassifier()
arvore.fit(x,y)

# %%
import matplotlib.pyplot as plt

plt.figure(dpi=600)

# passando pro metodo a arvore, pedindo pra arvore mostrar oq ela aprendeu
tree.plot_tree(arvore,
               class_names=arvore.classes_,
               feature_names=features,
               filled=True)
# %%
# ['Arredondada','Suculenta','Vermelha','Doce']

# novas predições para a arvore
# predict ja me da o resultadi da probabilidade
# se tiver empate na probabilidade, ele retorna em ordem alfgabetica
arvore.predict([[1,0,0,1]])

# %%

# lista de probabilidades, uma probabilidade para cada classe, uma probabilidade para cada fruta
# predict_proba me da uma lista com a probabilidade para cada frutas
# se tiver empate na probabilidade, ele retorna em ordem alfgabetica
probas = arvore.predict_proba([[1,1,1,1]])[0]
pd.Series(probas, index=arvore.classes_)