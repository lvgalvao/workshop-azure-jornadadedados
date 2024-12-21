# Bootcamp Cloud: Aula 01

## Introdução ao Azure e Cloud Computing

**Objetivo:** Fornecer uma introdução prática ao uso do Azure, abordando a criação de contas, controle de custos e navegação na interface gráfica, com foco em aplicações na área de dados.

---

## 1. Por que Utilizar Cloud?

1. **Escalabilidade:** O Azure permite escalar recursos conforme necessário, sem a necessidade de grandes investimentos iniciais.
2. **Custo-eficiência:** Com o Azure, você paga apenas pelo que utiliza, reduzindo custos operacionais.
3. **Acessibilidade:** Serviços de nuvem podem ser acessados de qualquer lugar, facilitando a colaboração e o trabalho remoto.
4. **Segurança:** O Azure oferece robustos recursos de segurança, incluindo criptografia e autenticação multifator.

## 2. O que Não é Cloud

1. **Não é um Data Center On-Premise:** Embora a nuvem envolva servidores, não é o mesmo que ter um data center físico na empresa.
2. **Não é apenas armazenamento:** A nuvem envolve muito mais do que apenas guardar dados. É um ecossistema completo de serviços.
3. **Não é sempre barato:** Se mal gerido, o uso da nuvem pode resultar em custos inesperados.

## 3. Acessando o Portal do Azure

1. **Portal do Azure:** Visite [portal.azure.com](https://portal.azure.com).
2. **Idioma do Portal:**
   - O idioma pode ser configurado na conta do usuário.
   - **Motivo:** O inglês é o idioma predominante em certificações, documentação, vagas de emprego e na própria interface do Azure.

## 4. Cadastro e Configuração Inicial da Conta Azure

**Criar uma Conta no Azure:**
1. Acesse o site oficial do Azure (azure.microsoft.com) e clique em "Iniciar gratuitamente".
2. Insira as informações solicitadas, como e-mail, senha e nome da conta.
3. Forneça as informações de pagamento (cartão de crédito/débito) para acessar os créditos gratuitos.
4. Verifique a conta via e-mail e complete o processo de criação.

**Configurações Iniciais:**
- O Azure oferece **200 USD em créditos gratuitos** no primeiro mês e uma camada gratuita de serviços essenciais.
- Após o cadastro, revise as configurações de segurança e habilite a autenticação multifator (MFA) para proteger a conta.

## 5. Controle de Custos no Azure

**Evitar Custos Inesperados:**
- **Azure Cost Management:** Use o Cost Management para configurar alertas de custo. Defina orçamentos mensais e configure notificações por e-mail.
- **Azure Pricing Calculator:** Utilize a calculadora de preços para estimar custos antes de provisionar recursos.

**Dicas Práticas:**
- Defina **limites de serviço** para evitar provisionamento excessivo.
- Revise regularmente os recursos em uso e encerre aqueles que não são necessários.

## 6. Navegação no Portal do Azure

**Azure Portal:**
- O **Azure Portal** é o painel de controle principal do Azure. Ele oferece acesso a todos os serviços disponíveis, como Storage Account, Virtual Machines e SQL Database.

**Serviços Comuns:**
- **Blob Storage:** Armazenamento escalável de objetos, ideal para dados brutos, backups e arquivos de grande volume.
- **Virtual Machines (VM):** Serviço que permite criar e gerenciar máquinas virtuais na nuvem.
- **Azure SQL Database:** Serviço gerenciado de banco de dados relacional, que suporta várias arquiteturas.

**Documentação e Suporte:**
- O Azure oferece documentação abrangente e suporte direto no portal. Acesse a documentação para obter informações detalhadas sobre cada serviço e suas configurações.

## 7. Visão Geral dos Produtos Azure

1. **Explorando Todos os Produtos:**
   - Navegue até a seção "Todos os serviços" no menu principal.
   - Explore as diversas categorias: Computação, Armazenamento, Banco de Dados, etc.

2. **Máquinas Virtuais (VM):**
   - **Visão Geral:** Serviço que permite criar instâncias de servidores virtuais.
   - **Tipos de Instâncias:** De uso geral, otimizadas para memória, para computação, etc.
   - **Democratização:** A nuvem democratiza o acesso a tecnologias avançadas.

3. **Visão Geral de Bancos de Dados:**
   - **Azure SQL Database:** Gerencia bancos de dados como MySQL e PostgreSQL.
   - **Cosmos DB:** Banco de dados NoSQL globalmente distribuído.
   - **Data Lake Storage:** Solução para análise e armazenamento de grandes volumes de dados.

## 8. Configuração de Regiões

**Regiões e Zonas de Disponibilidade:**
- **Regiões** são locais geográficos onde o Azure mantém seus data centers. Cada região possui várias **Zonas de Disponibilidade**, que são grupos de data centers fisicamente separados.
- A escolha da região influencia a latência dos serviços e pode ter implicações legais e de conformidade.

**Escolha da Região:**
- Selecione a região mais próxima dos seus usuários ou que atenda aos requisitos específicos do projeto.

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
     - **Nome:** Escolha um nome único (exemplo: `Workshop-Cloud-Dados`).
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

### 4. Criando um Website estático

1. **Em Data Management**
    - Data Management, clique em **Static Website** para adicionar arquivos.
    - Clique em **Enabled**

Index document name
```bash
index.html
```

Error document path
```bash
404.html
```

Após isso vai receber sua Primary endpoint

[cloudstorageworkshop](https://cloudstorageworkshop.z13.web.core.windows.net/)

1. **Em data storage**
   - Vai para o $web

2. **Upload de Arquivos:**
   
   - Vamos criar o Index e o error 404.html
   - Vamos tirar o Print da Foto
   - Dentro do container, clique em **Upload** para adicionar arquivos.

3. **Acessando Arquivos Publicamente:**
   - Arquivos podem ser acessados via URL, dependendo das permissões configuradas.

4. **Configuração de Ciclo de Vida:**
   - Vá até a aba **Lifecycle Management**.
   - Configure regras para mover dados entre camadas (ex: mover para Archive após 30 dias).

### **Conclusão**
O Azure Blob Storage é uma alternativa poderosa e escalável ao Amazon S3, oferecendo funcionalidades equivalentes com integração nativa ao ecossistema do Azure. O aprendizado e adaptação de conceitos entre AWS e Azure são essenciais para profissionais de Cloud e Engenharia de Dados, garantindo flexibilidade em projetos multicloud.

#### Olhando mais detalhes do 