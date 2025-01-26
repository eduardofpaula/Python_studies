# %%
import pandas as pd

# %%

# lendo o arquivo csv
df_customer = pd.read_csv('../data/customers.csv', sep=';')
df_customer
# %%
# lendo o arquivo excel
df_transactions = pd.read_excel('../data/transactions.xlsx')
df_transactions

# %%
# lendo o arquivo parquet
df_transaction_product = pd.read_parquet('../data/transactions_cart.parquet')
df_transaction_product
# %%

# join do dataframe transactions com o dataframe customer
df_join_transaction_customer = df_transactions.merge(
    df_customer,
    how='inner',
    left_on='IdCustomer',
    right_on='UUID',
    suffixes=['_transacao', '_cliente'],
)

# %%

# join do dataframe df_join_transaction_customer com o dataframe df_transaction_product
df_join_transaction_customer.merge(
    df_transaction_product,
    how='inner',
    left_on='UUID_transacao',
    right_on='IdTransaction',
)
