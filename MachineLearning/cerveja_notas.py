# %%

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('../MachineLearning/data/dados_cerveja_nota.xlsx')
df

# %%

# Gráfico de dispersão, nota x cerveja, 'o' é o tipo de marcador
plt.plot(df['cerveja'],df['nota'],'o')
# adiciona grid no fundo do gráfico
plt.grid(True)
# Título do gráfico
plt.title('Relação Nota x Cerveja')
# limite do eixo y e x
plt.ylim(0,12)
plt.xlim(0,11)
# Rótulo do eixo y e x
plt.ylabel('Nota')
plt.xlabel('Cerveja')
# para mostrar o gráfico
plt.show()
# %%
from sklearn import linear_model

# cria um objeto de regressão linear
reg = linear_model.LinearRegression()
reg.fit(df[['cerveja']],df['nota'])

# %%
# meu coeficiente que é meu B, quanta cerveja aumenta a nota
reg.coef_
# %%
# meu intercepto que é meu A, onde a reta corta o eixo y
reg.intercept_

# %%
# intercepto e coeficiente
a,b = reg.intercept_,reg.coef_[0]
print(f'a= {a}, b= {b}')
# %%

# linha de regressão
X = df[['cerveja']].drop_duplicates()
y_estimado = reg.predict(X)
y_estimado

plt.plot(df['cerveja'],df['nota'],'o')
plt.plot(X,y_estimado,'-')
plt.grid(True)
plt.title('Relação Nota x Cerveja')
plt.ylim(0,12)
plt.xlim(0,11)
plt.ylabel('Nota')
plt.xlabel('Cerveja')
plt.show()


# %%

# modelo de arvore de decisão
from sklearn import tree
# diminuir a profundidade da árvore para 2 para se obter um modelo mais linear
arvore = tree.DecisionTreeRegressor(max_depth=2)
arvore.fit(df[['cerveja']],df['nota'])

y_estimado_arvore = arvore.predict(X)
y_estimado_arvore

plt.plot(df['cerveja'],df['nota'],'o')
plt.plot(X,y_estimado,'-')
plt.plot(X,y_estimado_arvore,'-')
plt.grid(True)
plt.title('Relação Nota x Cerveja')
plt.ylim(0,12)
plt.xlim(0,11)
plt.ylabel('Nota')
plt.xlabel('Cerveja')
plt.legend(['Pontos','Regressão Linear','Árvore de Decisão']) 
plt.show()

# o grafico mostra a relação entre a cerveja e a nota, e dois modelos para mostrar qual seria a nota esperada com base na quantidade de cerveja 