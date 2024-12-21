import logging
import azure.functions as func
import requests
from datetime import datetime

app = func.FunctionApp()

def extrair_dados_bitcoin():
    """Extrai o JSON completo da API da Coinbase."""
    url = 'https://api.coinbase.com/v2/prices/spot'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        logging.error(f"Erro na API: {resposta.status_code}")
        return None

def tratar_dados_bitcoin(dados_json):
    """Transforma os dados brutos da API e adiciona timestamp."""
    valor = float(dados_json['data']['amount'])
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    timestamp = datetime.now()

    dados_tratados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": timestamp
    }
    return dados_tratados

@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False)
def timer_trigger_generate_number(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.warning('A execução do timer está atrasada!')

    # Extrai os dados da API
    dados_brutos = extrair_dados_bitcoin()
    if dados_brutos:
        # Transforma os dados extraídos
        dados_tratados = tratar_dados_bitcoin(dados_brutos)
        
        # Registra os dados tratados nos logs
        logging.info(f"Dados do Bitcoin: {dados_tratados}")
    else:
        logging.error("Falha ao processar os dados do Bitcoin.")
