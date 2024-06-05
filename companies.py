import pandas as pd
import sqlite3

# Carregar os dados do arquivo CSV
df = pd.read_csv('cias_abertas.csv', usecols=['CNPJ_CIA', 'DENOM_SOCIAL', 'SIT'], sep=';')

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('companies.db')

# Salvar os dados no banco de dados
df.to_sql('dados_empresas', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()

print('Dados importados com sucesso')