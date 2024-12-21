import azure.functions as func
import json

# Dicionário de fontes de dados e seus status
data_sources = {
    'SalesDB': 'Ativo',
    'MarketingAPI': 'Ativo',
    'CustomerDataLake': 'Inativo',
    'InventoryService': 'Ativo',
    'AnalyticsDB': 'Ativo',
}

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="datasources/{source_id?}", methods=["GET"])
def GetDataSource(req: func.HttpRequest) -> func.HttpResponse:
    """
    Obtém o status de uma fonte de dados específica ou retorna todas as fontes de dados.
    
    GET /datasources/{source_id?}
    """
    # O ID da fonte de dados é parte do caminho da URL e é opcional
    source_id = req.route_params.get('source_id', None)

    if source_id:
        status = data_sources.get(source_id)
        if not status:
            return func.HttpResponse(
                 f"A fonte de dados '{source_id}' não foi reconhecida.",
                 status_code=404
            )
        return func.HttpResponse(json.dumps({'status': status}), mimetype="application/json")
    else:
        # Se nenhum ID for fornecido, retorna a lista completa
        return func.HttpResponse(json.dumps(data_sources), mimetype="application/json")

@app.route(route="datasources/{source_id}", methods=["DELETE"])
def DeleteDataSource(req: func.HttpRequest) -> func.HttpResponse:
    """
    Remove uma fonte de dados específica do dicionário.
    
    DELETE /datasources/{source_id}
    """
    method = req.method
    if method == 'DELETE':
        # Lidar com a requisição DELETE
        source_id = req.route_params.get('source_id', None)
        if source_id in data_sources:
            del data_sources[source_id]
            return func.HttpResponse(f"Fonte de dados: {source_id} foi deletada.", status_code=200)
        else:
            return func.HttpResponse(f"Fonte de dados: {source_id} não encontrada.", status_code=404)
    else:
        return func.HttpResponse("Este método HTTP não é suportado.", status_code=405)
