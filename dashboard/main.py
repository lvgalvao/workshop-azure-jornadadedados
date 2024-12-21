import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Configurações do Key Vault
KEY_VAULT_URL = "https://azurekeyvaultworkshop.vault.azure.net/"
SERVER = "workshopazuredatavase.database.windows.net"
DATABASE = "bitcoin_database"
DRIVER = "ODBC Driver 18 for SQL Server"

# Configuração da página (primeiro comando Streamlit)
st.set_page_config(page_title="Dashboard de Preços do Bitcoin", layout="wide")

# Função para buscar segredos do Azure Key Vault
def get_secrets_from_key_vault():
    try:
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=KEY_VAULT_URL, credential=credential)
        sql_username = client.get_secret("sqlusername").value
        sql_password = client.get_secret("sqlpassword").value
        return sql_username, sql_password
    except Exception as e:
        st.error(f"Erro ao obter segredos do Key Vault: {e}")
        return None, None

# Função para ler os dados do SQL Server
def ler_dados_sqlserver():
    try:
        sql_username, sql_password = get_secrets_from_key_vault()
        if not sql_username or not sql_password:
            return pd.DataFrame()

        # Configurar conexão SQLAlchemy
        connection_string = (
            f"mssql+pyodbc://{sql_username}:{sql_password}@{SERVER}/{DATABASE}?driver={DRIVER.replace(' ', '+')}"
        )
        engine = create_engine(connection_string)

        # Testar conexão
        try:
            with engine.connect() as conn:
                st.success("Conexão com o banco de dados estabelecida com sucesso!")
        except Exception as ex:
            st.error(f"Erro ao conectar no SQL Server: {ex}")
            return pd.DataFrame()

        # Executar consulta
        query = "SELECT * FROM BitcoinData ORDER BY timestamp DESC"
        df = pd.read_sql(query, engine)
        return df
    except Exception as ex:
        st.error(f"Erro ao conectar ou executar consulta no SQL Server: {ex}")
        return pd.DataFrame()

# Função principal
def main():
    st.title("📊 Dashboard de Preços do Bitcoin")
    st.write("Este dashboard exibe os dados do preço do Bitcoin coletados periodicamente em um banco SQL Server.")

    df = ler_dados_sqlserver()

    if not df.empty:
        st.subheader("📋 Dados Recentes")
        st.dataframe(df)

        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values(by='timestamp')

        st.subheader("📈 Evolução do Preço do Bitcoin")
        st.line_chart(data=df, x='timestamp', y='valor', use_container_width=True)

        st.subheader("🔢 Estatísticas Gerais")
        col1, col2, col3 = st.columns(3)
        col1.metric("Preço Atual", f"${df['valor'].iloc[-1]:,.2f}")
        col2.metric("Preço Máximo", f"${df['valor'].max():,.2f}")
        col3.metric("Preço Mínimo", f"${df['valor'].min():,.2f}")
    else:
        st.warning("Nenhum dado encontrado no banco de dados SQL Server.")

if __name__ == "__main__":
    main()
