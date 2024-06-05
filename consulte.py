import sqlite3

def consultar_empresa(cnpj_cia):
    conn = sqlite3.connect('companies.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dados_empresas WHERE CNPJ_CIA = ?", (cnpj_cia,))
    empresa = cursor.fetchone()

    if empresa:
        print("CNPJ_CIA:", empresa[0])
        print("DENOM_SOCIAL:", empresa[1])
        print("SIT:", empresa[2])
    else:
        print("Empresa não encontrada.")

    conn.close()

while True:
    cnpj_cia = input("Digite o CNPJ_CIA para consultar (ou 'sair' para sair): ")
    
    if cnpj_cia.lower() == 'sair':
        break
    
    consultar_empresa(cnpj_cia)