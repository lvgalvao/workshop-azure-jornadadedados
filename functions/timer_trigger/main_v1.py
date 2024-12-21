import logging
import os
import requests
from datetime import datetime
import azure.functions as func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, String, Integer, DateTime
from datetime import datetime

# Cria a classe Base do SQLAlchemy (na versão 2.x)
Base = declarative_base()

class BitcoinPreco(Base):
    """Define a tabela no banco de dados."""
    __tablename__ = "bitcoin_precos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float, nullable=False)
    criptomoeda = Column(String(50), nullable=False)  # até 50 caracteres
    moeda = Column(String(10), nullable=False)        # até 10 caracteres
    timestamp = Column(DateTime, default=datetime.now)

# Configurações do Banco de Dados a partir das variáveis de ambiente
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Monta a URL de conexão ao PostgreSQL
DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# Cria o engine e a sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def criar_tabela():
    """Cria a tabela no banco de dados, se não existir."""
    Base.metadata.create_all(engine)
    logging.info("Tabela criada/verificada com sucesso!")

def extrair_dados_bitcoin():
    """Extrai o JSON completo da API da Coinbase."""
    url = 'https://api.coinbase.com/v2/prices/spot'
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            logging.error(f"Erro na API: {resposta.status_code}")
            return None
    except requests.RequestException as e:
        logging.error(f"Erro na requisição à API: {e}")
        return None

def tratar_dados_bitcoin(dados_json):
    """Transforma os dados brutos da API e adiciona timestamp."""
    try:
        valor = float(dados_json['data']['amount'])
        criptomoeda = dados_json['data']['base']
        moeda = dados_json['data']['currency']
        timestamp = datetime.utcnow()
        
        dados_tratados = {
            "valor": valor,
            "criptomoeda": criptomoeda,
            "moeda": moeda,
            "timestamp": timestamp
        }
        return dados_tratados
    except (KeyError, ValueError, TypeError) as e:
        logging.error(f"Erro ao tratar dados: {e}")
        return None

def salvar_dados_postgres(dados):
    """Salva os dados no banco PostgreSQL."""
    session = Session()
    try:
        novo_registro = BitcoinPreco(**dados)
        session.add(novo_registro)
        session.commit()
        logging.info(f"[{dados['timestamp']}] Dados salvos no PostgreSQL!")
    except SQLAlchemyError as ex:
        logging.error(f"Erro ao inserir dados no PostgreSQL: {ex}")
        session.rollback()
    finally:
        session.close()

def pipeline_bitcoin():
    """Executa a pipeline de ETL do Bitcoin."""
    logging.info("Iniciando pipeline ETL do Bitcoin.")
    
    # Criar/verificar tabela
    criar_tabela()
    
    # Extrair Dados da API Coinbase
    dados_json = extrair_dados_bitcoin()
    if not dados_json:
        logging.error("Falha na extração dos dados. Abortando pipeline.")
        return
    
    # Tratar Dados do Bitcoin
    dados_tratados = tratar_dados_bitcoin(dados_json)
    if not dados_tratados:
        logging.error("Falha no tratamento dos dados. Abortando pipeline.")
        return
    
    # Salvar Dados no PostgreSQL
    salvar_dados_postgres(dados_tratados)
    
    logging.info("Pipeline ETL do Bitcoin finalizada com sucesso.")

# Inicializa a FunctionApp
app = func.FunctionApp()

@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=False,
                  use_monitor=False) 
def timer_trigger_generate_number(mytimer: func.TimerRequest) -> None:
    """Função principal executada pelo Timer Trigger."""
    utc_timestamp = datetime.utcnow().isoformat()
    
    if mytimer.past_due:
        logging.warning('A execução do timer está atrasada!')
    
    logging.info('Função iniciada em %s', utc_timestamp)
    try:
        pipeline_bitcoin()
    except Exception as e:
        logging.error(f"Erro inesperado na pipeline: {e}")
    logging.info('Função finalizada em %s', datetime.utcnow().isoformat())
