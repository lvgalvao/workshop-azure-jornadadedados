import logging
import os
import requests
from datetime import datetime, timezone
import azure.functions as func

# Se você precisar usar variáveis de ambiente, pode utilizar python-dotenv para desenvolvimento local
# e Application Settings no Azure para produção.
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env (apenas para desenvolvimento local)
load_dotenv()

def extrair_dados_bitcoin():
    """Extrai o JSON completo da API da Coinbase."""
    url = 'https://api.coinbase.com/v2/prices/spot'
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"Erro na API: {http_err}")
        return None
    except Exception as err:
        logging.error(f"Erro ao extrair dados da API: {err}")
        return None

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()

    if mytimer.past_due:
        logging.warning('O timer está atrasado!')

    logging.info(f'Função executada em {utc_timestamp}')

    dados_json = extrair_dados_bitcoin()

    if dados_json:
        logging.info(f"Dados recebidos da API: {dados_json}")
    else:
        logging.error("Falha ao obter dados da API.")
