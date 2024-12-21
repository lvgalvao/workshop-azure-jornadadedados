O diretório contém:

1. **`app/main.py`**: Código principal em Python.
2. **`Dockerfile`**: Configuração do ambiente Docker para rodar a aplicação.
3. **`docker-compose.yml`**: Gerencia a aplicação Docker e variáveis de ambiente.

### Para rodar o projeto:

1. **Crie o diretório e a estrutura mencionada.**
2. **Adicione o arquivo `requirements.txt` com as dependências:**
   ```plaintext
   streamlit
   pandas
   pyodbc
   azure-identity
   azure-keyvault-secrets
   ```

3. **Execute o comando para construir e rodar:**
   ```bash
   docker-compose up --build
   ```

A aplicação ficará disponível em [http://localhost:8501](http://localhost:8501).

### **Bibliotecas e sua Função**

1. **`streamlit`**
   - **Descrição**: Uma biblioteca Python para criar aplicativos de dashboard e interfaces web interativas de maneira rápida e simples.
   - **Uso no Código**: Utilizada para criar o dashboard e exibir dados, gráficos e métricas.
   - **Instalação**:
     ```bash
     pip install streamlit
     ```

2. **`pyodbc`**
   - **Descrição**: Uma biblioteca para conectar-se a bancos de dados que utilizam o protocolo ODBC, como SQL Server.
   - **Uso no Código**: Faz a conexão com o SQL Server e executa consultas SQL.
   - **Instalação**:
     ```bash
     pip install pyodbc
     ```

3. **`pandas`**
   - **Descrição**: Biblioteca essencial para manipulação e análise de dados em Python, incluindo suporte para estruturas como DataFrames.
   - **Uso no Código**: Lê os dados do SQL Server e os organiza em um DataFrame para serem exibidos no dashboard.
   - **Instalação**:
     ```bash
     pip install pandas
     ```

4. **`azure.identity`**
   - **Descrição**: Parte do SDK do Azure, fornece métodos de autenticação, como o `DefaultAzureCredential` para acessar serviços Azure usando credenciais gerenciadas.
   - **Uso no Código**: Realiza a autenticação com o Azure Key Vault para acessar segredos.
   - **Instalação**:
     ```bash
     pip install azure-identity
     ```

5. **`azure.keyvault.secrets`**
   - **Descrição**: Parte do SDK do Azure, permite interagir com o serviço Key Vault para gerenciar segredos (senhas, chaves e outros).
   - **Uso no Código**: Acessa os segredos armazenados no Key Vault, como usuário e senha do banco de dados.
   - **Instalação**:
     ```bash
     pip install azure-keyvault-secrets
     ```

---

### **Instalação de Todas as Dependências de Uma Vez**
Crie um arquivo `requirements.txt` com o seguinte conteúdo:

```plaintext
streamlit
pyodbc
pandas
azure-identity
azure-keyvault-secrets
```

Depois, execute:

```bash
pip install -r requirements.txt
```

Isso garantirá que todas as bibliotecas sejam instaladas corretamente. 

Se precisar de mais detalhes sobre alguma biblioteca ou sua configuração, é só pedir!