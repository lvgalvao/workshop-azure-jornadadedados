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

### 9.1 Criando uma Conta de Armazenamento

1. **Nome da Conta:**
   - Escolha um nome único. O nome deve ser globalmente único dentro do Azure.
  
2. **Localização:**
   - Selecione a região mais próxima dos seus usuários.

3. **Tipo de Conta:**
   - Escolha entre **Standard** (geralmente mais barato) ou **Premium** (melhor performance).

4. **Camadas de Acesso:**
   - Configure o nível de acesso: **Hot** (uso frequente), **Cool** (uso menos frequente) ou **Archive** (armazenamento a longo prazo).

5. **Tags:**
   - Adicione tags para identificar e organizar sua conta de armazenamento.

6. **Criptografia:**
   - Configure a criptografia padrão para garantir que todos os objetos armazenados sejam criptografados automaticamente.

### 9.2 Configurando um Blob Storage

1. **Criar um Container:**
   - No portal do Azure, crie um container dentro da conta de armazenamento.
   - Configure as permissões (Privado, Blob, ou Público).

2. **Upload de Arquivo:**
   - Faça upload de arquivos no container.

3. **Acesso Público:**
   - Configure permissões para tornar os arquivos acessíveis publicamente, se necessário.

### 9.3 Habilitando um Website Estático

1. **Configuração:**
   - Habilite a opção de hospedagem de site estático na conta de armazenamento.
   - Defina o documento de índice, como `index.html`.

2. **Acessando o Site:**
   - Use a URL fornecida pelo Azure para acessar o site estático.

---

## 10. Criando e Configurando uma Máquina Virtual (VM)

### 10.1 Configurando a Máquina Virtual

1. **Criar uma VM:**
   - Escolha o tipo de imagem (Windows, Linux) e tamanho da instância.
   - Configure a rede virtual, NSG (Network Security Group) e outros parâmetros.

2. **Conexão via SSH:**
   - Use o comando SSH para conectar-se à VM:

   ```bash
   ssh -i "caminho-da-chave.pem" usuario@ip-publico
   ```

3. **Instalar Python e Aplicações:**
   - Configure o ambiente instalando Python, `pip3` e Streamlit.

---

Essa estrutura substitui todos os aspectos da AWS para o equivalente no Azure, mantendo as funcionalidades principais e adaptando ao ambiente da Microsoft. Caso precise de ajustes adicionais, basta me avisar!