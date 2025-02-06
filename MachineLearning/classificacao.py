# %%

import pandas as pd

df = pd.read_excel('../MachineLearning/data/dados_cerveja_nota.xlsx')
df

# %%

df['Aprovado'] = df['nota'] >= 5
df

# %%

from sklearn import linear_model
reg = linear_model.LogisticRegression(penalty=None,
                                      fit_intercept=True)

features = ['cerveja']
target = 'Aprovado'

# aqui o modelo aprende
reg.fit(df[features],df[target])

# aqui o modelo prevê
reg_predict = reg.predict(df[features])
reg_predict
# %%
from sklearn import metrics

# comparando os dois modelos
# acurácia é a quantidade de acertos dividido pelo total
reg_acc = metrics.accuracy_score(df[target],reg_predict)
reg_acc
# %%
# matriz de confusão

# matriz de confusão ajuda a entender o desempenho do classificador
# True Positivo (TP) - classificado como positivo e é positivo
# True Negativo (TN) - classificado como negativo e é negativo
# False Positivo (FP) - classificado como positivo e é negativo
# False Negativo (FN) - classificado como negativo e é positivo
reg_conf = metrics.confusion_matrix(df[target],reg_predict)
print(reg_conf)
reg_conf = pd.DataFrame(reg_conf,
                        index=['False','True'],
                        columns=['False','True'],)
reg_conf
# %%
from sklearn import tree
arvore = tree.DecisionTreeClassifier(max_depth=3)

# aqui o modelo aprende
arvore.fit(df[features], df[target])

# aqui o modelo prevê
arvore_predict = arvore.predict(df[features])
arvore_predict

arvore_acc = metrics.accuracy_score(df[target], arvore_predict)
print("Acurácia Árvore:", arvore_acc)

arvore_precision = metrics.precision_score(df[target], arvore_predict)
print("Precisão Árvore:", arvore_precision)

arvore_recall = metrics.recall_score(df[target], arvore_predict)
print("Recall Árvore:", arvore_recall)

arvore_conf = metrics.confusion_matrix(df[target], arvore_predict)
arvore_conf