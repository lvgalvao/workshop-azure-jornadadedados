### **Passos para Criar o Projeto e Adicionar o Código**

- Instalar Extensões
- Instalar CLI
- Instalar pip

#### **1. Criar um Novo Projeto de Azure Functions**
1. **Abra o VS Code** e certifique-se de que a extensão **Azure Functions** está instalada.
2. Pressione `Ctrl+Shift+P` e selecione **Azure Functions: Create New Project**.
3. Escolha o diretório onde deseja criar o projeto.
4. Selecione **Python** como a linguagem.
5. Escolha o **trigger HTTP** como modelo inicial.
6. Configure as opções:
   - **Function name**: `ManageDataSources`.
   - **Authorization level**: **Function**.

---

#### **2. Adicionar o Código no Arquivo `__init__.py`**

Substitua o conteúdo gerado automaticamente pelo seguinte código:

```python
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
    source_id = req.route_params.get('source_id', None)
    if source_id in data_sources:
        del data_sources[source_id]
        return func.HttpResponse(f"Fonte de dados: {source_id} foi deletada.", status_code=200)
    else:
        return func.HttpResponse(f"Fonte de dados: {source_id} não encontrada.", status_code=404)
```

---

### **3. Instalar Dependências**

Certifique-se de que o arquivo `requirements.txt` contenha as dependências necessárias. Adicione o pacote `azure-functions` ao arquivo:
```text
azure-functions
```

No terminal, execute:
```bash
pip install -r requirements.txt
```

---

### **4. Testar Localmente**

1. **Inicie o servidor local:**
   No terminal do VS Code, execute:
   ```bash
   func start
   ```
2. **Acesse os endpoints:**
   - Para obter a lista de fontes de dados:
     ```
     GET http://localhost:7071/api/datasources
     ```
   - Para obter o status de uma fonte específica:
     ```
     GET http://localhost:7071/api/datasources/SalesDB
     ```
   - Para deletar uma fonte de dados:
     ```
     DELETE http://localhost:7071/api/datasources/SalesDB
     ```

   Use um navegador, **Postman**, ou **cURL** para testar as requisições.

---

### **5. Implantar no Azure**

1. **Faça login no Azure:**
   Pressione `Ctrl+Shift+P` e selecione **Azure: Sign In**.

2. **Crie um Function App no Azure:**
   - Clique no ícone do Azure na barra lateral.
   - Clique com o botão direito em **Functions** e selecione **Create Function App in Azure**.
   - Escolha um nome único e as configurações do runtime.

3. **Implante a função:**
   - Pressione `Ctrl+Shift+P` e selecione **Azure Functions: Deploy to Function App**.
   - Escolha o projeto local e o Function App criado.

---

### **Resumo do Funcionamento**
- **Endpoint `GET`**:
  - Sem um `source_id`, retorna todos os dados.
  - Com um `source_id`, retorna o status da fonte específica.
- **Endpoint `DELETE`**:
  - Remove a fonte de dados se ela existir, ou retorna um erro 404 se não for encontrada.

Se precisar de mais ajuda, é só perguntar!