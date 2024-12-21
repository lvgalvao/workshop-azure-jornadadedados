# Bootcamp Cloud: Parte 02

## Armazenamento de Dados no Azure (Blob Storage) e Comparação com AWS (S3)

**Objetivo:** Explorar as diversas aplicações do Azure Blob Storage no contexto de engenharia, ciência e análise de dados. Será feita uma comparação prática com o Amazon S3, destacando diferenças e similaridades. Além disso, aprenderemos a criar e configurar contas de armazenamento, containers e permissões no Azure.

### 1. O que é Storage? Azure vs AWS

1. **Definição:**
   - Storage refere-se ao espaço onde dados digitais são armazenados. No **Azure**, o serviço equivalente ao **S3** da AWS é o **Azure Blob Storage**.

2. **Comparação entre Azure Blob Storage e Amazon S3:**

| Característica           | Azure Blob Storage                         | Amazon S3                                |
|--------------------------|--------------------------------------------|------------------------------------------|
| **Tipo de Armazenamento** | Armazenamento de objetos                   | Armazenamento de objetos                 |
| **Camadas de Acesso**     | Hot, Cool, Archive                         | Standard, Intelligent-Tiering, Glacier   |
| **Redundância**           | LRS, GRS, ZRS, RA-GRS                      | Standard (3 AZs), One Zone-IA, Glacier   |
| **Hospedagem Estática**   | Suporte parcial (via Azure CDN)            | Suporte nativo                           |
| **Gerenciamento de Ciclo**| Lifecycle Management via regras definidas  | Lifecycle Policies                       |
| **Integração com ML**     | Azure ML                                   | Amazon SageMaker                         |

---

## Grupo de Recurso

### **Como Criar um Grupo de Recursos no Azure para o Workshop**

O Grupo de Recursos será o contêiner principal para todos os recursos usados no workshop, permitindo organização e gerenciamento centralizado.

---

### **Passo a Passo para Criar um Grupo de Recursos**

#### **1. Acesse o Azure Portal**
- Faça login no [Azure Portal](https://portal.azure.com).

#### **2. Navegue até "Grupos de Recursos"**
- No menu lateral, clique em **"Grupos de Recursos"**.
- Se não estiver visível, procure por **"Grupos de Recursos"** na barra de pesquisa superior.

#### **3. Clique em "Criar"**
- Na página de Grupos de Recursos, clique no botão **"Criar"** para iniciar o processo.

#### **4. Configure o Grupo de Recursos**
- Preencha os campos necessários:
  - **Assinatura:** Selecione a assinatura onde o grupo será criado.
  - **Grupo de Recursos:** Insira o nome do grupo. Escolha um nome descritivo, como `Workshop-Cloud-Dados`.
  - **Região:** Escolha a região onde os recursos do workshop serão gerenciados. Se os participantes do workshop são locais, escolha a região mais próxima. Exemplo: `East US`.

#### **5. (Opcional) Adicione Tags**
- As **tags** ajudam a categorizar o grupo de recursos.
  - Exemplo:
    - **Key:** `Projeto`
    - **Value:** `Workshop-Cloud`

    Aqui está uma sugestão de tags para o grupo de recursos do workshop:

---

### **Tags para o Grupo de Recursos**

| **Chave (Key)**      | **Valor (Value)**         | **Descrição**                                 |
|-----------------------|---------------------------|-----------------------------------------------|
| **Projeto**          | `Workshop-Cloud`         | Nome do projeto associado ao grupo de recursos. |
| **Data**             | `21/12/2024`             | Data de realização do workshop.               |
| **Professor**        | `Luciano Vasconcelos`    | Nome do professor responsável pelo workshop.  |
| **Participantes**    | `100`                    | Número de profissionais participantes.        |
| **Ambiente**         | `Produção`               | Ambiente associado (ex.: produção, teste).    |
| **Tipo**             | `Educação`               | Categoria do projeto (ex.: educação, pesquisa). |
| **Região**           | `East US`                | Região onde o grupo de recursos será gerenciado. |
| **Departamento**     | `Engenharia de Dados`    | Área de foco do workshop.                     |
| **Responsável**      | `Luciano Vasconcelos`    | Responsável pelo grupo de recursos.           |

---

Essas tags ajudarão na organização e monitoramento dos recursos do workshop, facilitando o rastreamento e a categorização no futuro.

#### **6. Revise e Crie**
- Clique em **"Revisar e Criar"**.
- Após a validação, clique em **"Criar"**.

---

### **Por que Criar um Grupo de Recursos para o Workshop?**
- **Organização:** Todos os recursos do workshop (máquinas virtuais, contas de armazenamento, redes, etc.) estarão agrupados em um único local.
- **Gerenciamento Centralizado:** Facilita o controle de acesso e a aplicação de políticas.
- **Monitoramento de Custos:** Permite monitorar o custo total do workshop em um único painel.
- **Encerramento Simplificado:** Após o término do workshop, é possível excluir todo o grupo de recursos, apagando todos os recursos associados de forma eficiente.

---

### **Dicas para o Workshop**
- Crie políticas no nível do grupo para limitar o tipo de recursos que podem ser criados.
- Atribua permissões de acesso específicas ao grupo para os participantes, utilizando o Azure RBAC (Role-Based Access Control).
- Monitore o uso e os custos dentro do grupo de recursos durante o workshop através do **Azure Cost Management**.

### 2. Criação de Contas de Armazenamento no Azure

### 2.1 Criando uma Conta de Armazenamento

1. **Acesse o Azure Portal:**
   - Faça login no [Azure Portal](https://portal.azure.com).

2. **Crie uma Nova Conta de Armazenamento:**
   - Clique em **Criar um Recurso** e procure por **Storage Account**.
   - Configure os seguintes campos:
     - **Assinatura e Grupo de Recursos:** Escolha a assinatura e crie ou selecione um grupo de recursos.
     - **Nome:** Escolha um nome único (exemplo: `meu-storage-dados`).
     - **Região:** Escolha a região mais próxima dos usuários ou do processamento de dados.
     - **Performance:** Escolha entre Standard (mais barato) ou Premium (melhor performance).
     - **Redundância:** Opções incluem:
       - LRS (Locally Redundant Storage)
       - GRS (Geo-Redundant Storage)
       - ZRS (Zone-Redundant Storage)

3. **Configurações Avançadas:**
   - Ative criptografia com chave gerenciada pelo Azure ou pelo cliente.
   - Configure a política de acesso público.

4. **Criar a Conta de Armazenamento:**
   - Revise as configurações e clique em **Criar**.

---

### 4. Trabalhando com Containers no Azure Blob Storage

1. **Criando um Container:**
   - Acesse a conta de armazenamento criada.
   - Na aba **Containers**, clique em **+ Container**.
   - Nomeie o container (ex: `dados-brutos`) e configure permissões:
     - **Privado:** Apenas o proprietário da conta pode acessar.
     - **Público:** Permite leitura anônima.

2. **Upload de Arquivos:**
   - Dentro do container, clique em **Upload** para adicionar arquivos.

3. **Acessando Arquivos Publicamente:**
   - Arquivos podem ser acessados via URL, dependendo das permissões configuradas.

4. **Configuração de Ciclo de Vida:**
   - Vá até a aba **Lifecycle Management**.
   - Configure regras para mover dados entre camadas (ex: mover para Archive após 30 dias).

---

### 5. Recursos Avançados do Blob Storage

1. **Criptografia:**
   - Dados armazenados no Blob Storage são criptografados por padrão com AES-256.

2. **Redundância:**
   - Opções de redundância garantem alta disponibilidade:
     - **LRS:** Redundância local em um único data center.
     - **GRS:** Replicação entre regiões geograficamente distantes.

3. **Logging e Monitoramento:**
   - Use **Azure Monitor** para rastrear acessos e modificações nos dados.

4. **Event Grid:**
   - Configure eventos para disparar ações automatizadas, como notificações ou funções Azure.

---

### 6. Comparação Prática: S3 x Blob Storage

| Operação                  | AWS S3 Command                        | Azure Blob Storage Command               |
|---------------------------|----------------------------------------|------------------------------------------|
| **Criar Bucket/Container**| `aws s3 mb s3://bucket-name`          | `az storage container create`            |
| **Upload de Arquivo**     | `aws s3 cp file.txt s3://bucket-name` | `az storage blob upload`                 |
| **Download de Arquivo**   | `aws s3 cp s3://bucket-name/file.txt` | `az storage blob download`               |
| **Definir ACL**           | Via Bucket Policy                     | Via Blob Access Policy                   |
| **Configuração Lifecycle**| `aws s3api put-bucket-lifecycle`      | Configuração via Portal ou CLI           |

---

### 7. Exemplo Prático: Interagindo com o Blob Storage via Python

1. **Instalando o SDK do Azure:**
   ```bash
   pip install azure-storage-blob
   ```

2. **Código para Upload de Arquivos:**
   ```python
   from azure.storage.blob import BlobServiceClient

   # Configuração
   connection_string = "sua_connection_string"
   blob_service_client = BlobServiceClient.from_connection_string(connection_string)

   # Container e arquivo
   container_name = "dados-brutos"
   file_name = "arquivo.csv"

   # Upload
   blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
   with open(file_name, "rb") as data:
       blob_client.upload_blob(data)

   print(f"Arquivo {file_name} enviado para {container_name}.")
   ```

3. **Código para Download de Arquivos:**
   ```python
   # Download do Blob
   download_file_name = "downloaded_arquivo.csv"
   with open(download_file_name, "wb") as download_file:
       download_file.write(blob_client.download_blob().readall())

   print(f"Arquivo baixado como {download_file_name}.")
   ```

---

### 8. Casos de Uso do Blob Storage

1. **Data Lake no Azure:**
   - Combine Blob Storage com **Azure Data Lake** para criar um armazenamento escalável para dados brutos.
   - Integre com **Azure Data Factory** para pipelines ETL.

2. **Machine Learning:**
   - Use datasets armazenados no Blob Storage em **Azure Machine Learning** para treinar modelos.

3. **Arquivamento:**
   - Configure camadas Archive para dados que precisam ser retidos a longo prazo.

4. **Hospedagem de Sites Estáticos:**
   - Use Azure Blob Storage para hospedar páginas HTML simples.

---

### **Conclusão**
O Azure Blob Storage é uma alternativa poderosa e escalável ao Amazon S3, oferecendo funcionalidades equivalentes com integração nativa ao ecossistema do Azure. O aprendizado e adaptação de conceitos entre AWS e Azure são essenciais para profissionais de Cloud e Engenharia de Dados, garantindo flexibilidade em projetos multicloud.

#### Ver agora banco de dados