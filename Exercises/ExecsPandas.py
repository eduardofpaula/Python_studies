# %%
import pandas as pd
from datetime import datetime

# %%
# Ler o arquivo CSV em um DataFrame e exibir as primeiras 5 linhas.

df = pd.read_excel('../data/Execs/Pandas.csv')

# %%
# exibe as 5 primeiras linhas
df.head()
# %%
# Exibir as colunas e os tipos de dados do DataFrame.

# exibe informações do dataframe
df.info()
# %%
# Filtrar os funcionários do departamento "TI".
condicao = df['Departamento'] == 'TI'
df_TI = df[condicao]
df_TI
# %%

# Criar uma coluna chamada Salario_Anual multiplicando Salario por 12.
df['Salario_Anual'] = df['Salario'] * 12
df
# %%

# Ordenar os funcionários por Performance em ordem decrescente.

df_ordenados = df.sort_values(by='Performance', ascending=False).reset_index(
    drop=True
)
df_ordenados

# %%

# Selecionar os funcionários que trabalham na região "Sudeste" e estão ativos.
condicao = (df['Regiao'] == 'Sudeste') & (df['Ativo'] == 'Sim')
df_sudeste = df[condicao].reset_index(drop=True)
df_sudeste

# %%

# Criar uma coluna chamada Experiencia calculando o tempo de empresa com base em Ano_Contratacao.


def exp(ano_contrat: int):
    """
    função para calcular o tempo de experiencia com base no tempo de trabalho na empresa
    """
    anoAtual = datetime.now().year
    return anoAtual - ano_contrat


df['Experiencia'] = df['Ano_Contratacao'].apply(exp)
df
# %%
# Contar o número de funcionários por Regiao.
df_contagem = (
    df.groupby('Regiao').size().reset_index(name='Funcionarios_regiao')
)
df_contagem

# %%


def media(df):
    """
    função para calcular a média das horas semanais
    """
    df['Media_Horas_Departamento'] = df.groupby('Departamento')[
        'Horas_Semanais'
    ].transform('mean')
    return df


# Calcular a média de Horas_Semanais por Departamento.
df = media(df)
df

# %%
# Filtrar funcionários com salário acima de 4000 e idade inferior a 35.

condicao = (df['Salario'] > 4000) & (df['Idade'] < 35)
df[condicao].reset_index(drop=True)


# Renomear as colunas Performance para Desempenho e Horas_Semanais para Carga_Horaria.
# Criar uma nova coluna chamada Categoria_Salario classificando os salários em "Baixo", "Médio" ou "Alto".
# Criar um gráfico de barras com o número de projetos completados por Departamento.
# Calcular a soma total de Projetos_Completados por Regiao.
# Identificar o funcionário mais antigo (ano de contratação mais antigo).
# Remover os funcionários que não estão ativos.
# Exibir os 3 funcionários com melhor desempenho.
# Criar uma tabela pivô mostrando a média de Performance por Departamento e Regiao.
# Salvar o DataFrame atualizado em um novo arquivo chamado dados_processados.csv.
# Contar o número de funcionários com mais de 10 projetos completados.
# Exibir as linhas onde o Salario é nulo (se aplicável).
# Substituir valores nulos no Salario pela média salarial.
# Filtrar funcionários com desempenho menor que 4.0 e mais de 40 horas semanais.
# Agrupar os dados por Departamento e calcular o desvio padrão do Salario.
# Criar um histograma do Salario com intervalos de 500.
