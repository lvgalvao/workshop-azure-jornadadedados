### **Uso do Azure Blob Storage na Engenharia de Dados**

O **Azure Blob Storage** é uma solução de armazenamento de objetos no Azure que desempenha um papel crucial em projetos de **engenharia de dados**. Ele é altamente utilizado para construir pipelines de dados, armazenar dados brutos e processados, e integrar com ferramentas de análise e aprendizado de máquina.

---

### **Vantagens do Azure Blob Storage**

1. **Escalabilidade Ilimitada:**
   - Permite armazenar grandes volumes de dados, desde pequenos arquivos de log até datasets massivos, sem limites de crescimento prático.

2. **Baixo Custo:**
   - Oferece diversas camadas de armazenamento (Hot, Cool, Archive) que permitem otimizar custos com base na frequência de acesso aos dados.

3. **Alta Disponibilidade e Redundância:**
   - Suporta opções como **LRS (Locally Redundant Storage)** e **GRS (Geo-Redundant Storage)**, garantindo proteção contra falhas.

4. **Flexibilidade de Integração:**
   - Compatível com ferramentas como Azure Data Factory, Databricks, Synapse Analytics e frameworks de big data como Apache Spark.

5. **Compatibilidade com Formatos Populares:**
   - Suporta formatos de arquivos amplamente usados na engenharia de dados, como **CSV**, **Parquet**, e **JSON**.

6. **Suporte a Delta Lake e Iceberg:**
   - O Blob Storage suporta **Delta Lake** e **Apache Iceberg**, permitindo que arquiteturas de dados modernas sejam implementadas diretamente no Azure.

---

### **Por que o Azure Blob Storage é Amplamente Utilizado?**

1. **Centralização de Dados:**
   - Atua como um ponto único de armazenamento em pipelines **ETL/ELT** para consolidar dados de múltiplas fontes.

2. **Capacidade de Servir como Data Lake:**
   - Com Azure Data Lake Storage Gen2 integrado, ele se torna uma solução poderosa para armazenar dados brutos e processados.

3. **Compatibilidade com Ferramentas de Análise:**
   - É fácil de conectar ao Power BI, Azure Synapse Analytics e Azure Machine Learning para análises avançadas.

4. **Performance em Workloads Distribuídas:**
   - Compatível com clusters distribuídos, como Apache Spark, garantindo alta performance em processamento paralelo.

---

### **Exemplo de Arquiteturas Usando Azure Blob Storage**

#### **1. Data Lake com Blob Storage**
- **Arquitetura:**
  - O Blob Storage atua como uma camada de armazenamento central, onde:
    - **Bronze Layer:** Dados brutos são armazenados diretamente em formato **JSON** ou **CSV**.
    - **Silver layer:** Dados transformados em formatos otimizados, como **Parquet**.
    - **Gold layer:** Dados prontos para análise, organizados por data e departamento.
- **Ferramentas Conectadas:**
  - **Azure Data Factory:** Orquestra a movimentação e transformação dos dados.
  - **Azure Databricks:** Realiza transformações em larga escala.
  - **Azure Synapse Analytics:** Executa consultas analíticas em datasets prontos.

```
  sequenceDiagram
    participant Source as Fontes de Dados
    participant ADF as Azure Data Factory
    participant BlobBronze as Blob Storage (Bronze)
    participant BlobSilver as Blob Storage (Silver)
    participant BlobGold as Blob Storage (Gold)
    participant Databricks as Azure Databricks
    participant Synapse as Azure Synapse Analytics

    Source->>ADF: Envia dados brutos
    ADF->>BlobBronze: Armazena dados brutos (CSV, JSON)
    ADF->>Databricks: Ativa transformação
    Databricks->>BlobSilver: Salva dados processados (Parquet)
    Databricks->>BlobGold: Salva dados organizados para análise
    Synapse->>BlobGold: Consulta dados para relatórios
```

### **Compatibilidade com Delta Lake e Apache Iceberg**

- **Delta Lake:**
  - É totalmente compatível com o Azure Blob Storage.
  - Delta Lake adiciona **ACID transactions**, **schema enforcement**, e suporte a **time travel** ao Blob Storage.
  - Ideal para pipelines de dados complexos que exigem consistência e controle de versão.

- **Apache Iceberg:**
  - Também compatível com o Azure Blob Storage.
  - Iceberg é usado para gerenciar tabelas de dados em larga escala, oferecendo transações ACID e otimização para consultas.
  - É uma alternativa ao Delta Lake, com suporte mais nativo ao ecossistema Apache.

---

### **Projeto**

### **Projeto: Script de Backup para Mover Arquivos Locais para Azure Blob Storage**

A seguir está um passo a passo para criar um **script Python** que move arquivos de uma pasta local para o **Azure Blob Storage**. Este script é chamado de **script de backup** e utiliza o **Azure Storage Blob SDK**.

---

### **Passo 1: Pré-requisitos**

1. **Instalar o Python (3.6 ou superior):**
   - Certifique-se de que o Python esteja instalado no sistema.
   - Verifique a versão:
     ```bash
     python --version
     python -m venv .venv
     source .venv/Scripts/activate
     ```

2. **Instalar o SDK do Azure para Blob Storage:**
   - Use o pip para instalar o pacote necessário:
     ```bash
     pip install azure-storage-blob python-dotenv
     ```

3. **Credenciais de Acesso ao Azure:**
   - No Azure Portal:
     - Crie uma conta de armazenamento (Storage Account).
     - Gere a **connection string** no painel "Chaves de Acesso" da sua conta de armazenamento.

---

### **Passo 2: Estrutura do Projeto**
Organize os arquivos do projeto:
```
script-backup/
│
├── backup_script.py  # Script principal
├── local_files/      # Pasta com arquivos locais para backup
└── .env              # Variáveis de ambiente para connection string
```

---

### **Passo 3: Criar o Script Python**

#### **Arquivo `backup_script.py`**
```python
import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Variáveis de configuração
CONNECTION_STRING = os.getenv("AZURE_STORAGE_URL")
if not CONNECTION_STRING:
    raise ValueError("A connection string está vazia. Verifique o arquivo .env.")


CONTAINER_NAME = "backup"  # Nome do container no Azure
LOCAL_FOLDER = "./local_files"  # Caminho da pasta local para backup

def upload_files_to_blob():
    try:
        # Conectar ao Blob Storage
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)

        # Verificar se o container existe; se não, criar
        if not container_client.exists():
            container_client.create_container()
            print(f"Container '{CONTAINER_NAME}' criado.")

        # Iterar pelos arquivos na pasta local
        for root, _, files in os.walk(LOCAL_FOLDER):
            for file_name in files:
                local_file_path = os.path.join(root, file_name)

                # Nome do arquivo no Blob
                blob_name = os.path.relpath(local_file_path, LOCAL_FOLDER)

                # Upload do arquivo para o Blob
                with open(local_file_path, "rb") as data:
                    blob_client = container_client.get_blob_client(blob_name)
                    blob_client.upload_blob(data, overwrite=True)
                    print(f"Arquivo '{file_name}' enviado como '{blob_name}'.")

    except Exception as ex:
        print(f"Erro: {ex}")

if __name__ == "__main__":
    upload_files_to_blob()
```

---

### **Passo 4: Configurar as Credenciais**

#### **Arquivo `.env`**
Crie um arquivo `.env` no diretório do projeto e insira sua **connection string**:
```
AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=nome_da_conta;AccountKey=chave_de_acesso;EndpointSuffix=core.windows.net
```

---

### **Passo 5: Testar o Script**

1. **Adicionar Arquivos para Backup:**
   - Insira alguns arquivos na pasta `local_files/`.

2. **Executar o Script:**
   - No terminal, execute:
     ```bash
     python backup_script.py
     ```

3. **Verificar os Resultados:**
   - No Azure Portal, acesse o **container** no Blob Storage para confirmar que os arquivos foram enviados.

---

### **Explicação do Script**

1. **Conexão ao Blob Storage:**
   - Utiliza a connection string para se autenticar no serviço.

2. **Verificação e Criação do Container:**
   - Antes de fazer o upload, o script verifica se o container existe. Caso não exista, cria automaticamente.

3. **Iteração e Upload:**
   - Lê os arquivos de uma pasta local e os envia para o Blob Storage, preservando a estrutura de subdiretórios.

4. **Sobrescrita de Arquivos:**
   - Define `overwrite=True` no método `upload_blob` para garantir que arquivos com o mesmo nome sejam substituídos.

---

### **Melhorias Futuras**
1. **Logging:** Adicionar um sistema de logs para monitorar uploads.
2. **Compressão:** Compactar arquivos antes do upload.
3. **Agendamento:** Usar um agendador como **cron** (Linux) ou **Task Scheduler** (Windows) para executar o script periodicamente.

---

### **Resumo**
Esse script de backup é uma solução simples e eficiente para mover arquivos locais para o Azure Blob Storage, permitindo manter dados seguros na nuvem e facilitar processos de automação.