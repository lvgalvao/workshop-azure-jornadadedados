import logging
import azure.functions as func
import random  # Importa o módulo random para gerar números aleatórios
import requests

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=False,
                  use_monitor=False) 
def timer_trigger_generate_number(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.warning('A execução do timer está atrasada!')

    # Gera um número aleatório entre 1 e 6
    url = 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data['data']['amount']
        logging.info(f'Preço do Bitcoin: {price}')
    else:
        logging.error('Erro ao obter o preço do Bitcoin')
    # Registra o número gerado nos logs

