# Workshop Azure

## Cronograma

- **9:00** - Azure Quickstart, primeiro projeto online  
- **10:00** - Armazenamento de Dados no Azure  
- **11:00** - Python escalável com Azure VMs  
- **12:00** - Projeto I - ETL Extração de API no Azure
- **13:00** - Pausa para almoço
- **14:00** - Azure Active Directory e Azure Virtual Network  
- **15:00** - Projeto II - Serverless e Eventos no Azure  
- **16:00** - Fabric e próximos passos

## Introdução ao Azure e Cloud Computing

**Objetivo:** Fornecer uma introdução prática ao uso da Microsoft Azure, abordando a criação de contas, controle de custos e navegação na interface gráfica, com foco em aplicações na área de dados.

---

## 1. Por que Utilizar Cloud?

1. **Escalabilidade:** O Azure permite escalar recursos de acordo com a demanda, sem a necessidade de grandes investimentos iniciais.
2. **Custo-eficiência:** Com o Azure, você paga apenas pelo que utiliza, reduzindo custos operacionais e evitando gastos com infraestrutura ociosa.
3. **Acessibilidade:** Serviços de cloud podem ser acessados de qualquer lugar, facilitando a colaboração e o trabalho remoto.
4. **Segurança:** Provedores de cloud como a Microsoft investem fortemente em segurança, com recursos de criptografia, autenticação multifator e conformidade com padrões internacionais.

## 2. O que Não é Cloud

1. **Não é um Data Center On-Premise:** Embora a cloud envolva servidores, não é o mesmo que possuir um data center físico dentro da empresa.
2. **Não é apenas armazenamento:** A nuvem envolve muito mais do que apenas guardar dados. É um ecossistema completo de serviços: computação, banco de dados, análise de dados, inteligência artificial, etc.
3. **Não é sempre barato:** Má gestão de recursos na nuvem pode levar a custos inesperados. É fundamental monitorar gastos e otimizar recursos.

## 3. Acessando o Portal do Azure

1. **Site do Azure:** Visite [https://azure.microsoft.com](https://azure.microsoft.com).
2. **Portal do Azure:**
   - Acesse o [Portal do Azure](https://portal.azure.com) para gerenciar recursos.
   - Ajuste o idioma (se necessário) no canto superior direito, preferindo o inglês para se familiarizar com a linguagem de certificações, documentação e mercado de trabalho.

## 4. Cadastro e Configuração Inicial da Conta Azure

**Criar uma Conta no Azure:**
1. Acesse o site oficial do Azure ([azure.microsoft.com](https://azure.microsoft.com)) e clique em "Free account" ou "Create a free account".
2. Insira as informações solicitadas, como e-mail, senha e detalhes de cobrança (cartão de crédito/débito). A Microsoft não cobrará se você ficar dentro dos limites gratuitos.
3. Verifique a conta via e-mail e complete o processo de criação.

**Configurações Iniciais:**
- Opte pelo **Azure Free Account**, que oferece um crédito inicial e alguns serviços gratuitos por 12 meses, ideal para iniciantes.
- Após criar a conta, revise as configurações de segurança e habilite a autenticação multifator (MFA) por meio do Azure Active Directory (Azure AD).

## 5. Controle de Custos no Azure

**Evitar Custos Inesperados:**
- **Azure Cost Management + Billing:** Use o Cost Management para configurar alertas de custo, visualizar relatórios e orçamentos. Acesse pelo próprio portal e defina um orçamento mensal com notificações por e-mail.
- **Revisão de Recursos:** Monitore regularmente os recursos em uso. Encerre máquinas virtuais, bancos de dados e outros serviços não utilizados.

**Dicas Práticas:**
- Defina **limites de consumo** e use **tags** para categorizar recursos por ambiente, projeto ou centro de custo.
- Automatize a desativação ou redução de recursos ociosos.

## 6. Navegação na Interface Gráfica do Azure

**Portal do Azure:**
- O **Portal do Azure** é a interface gráfica central para gerenciar todos os serviços. Nele você acessa máquinas virtuais, contas de armazenamento, bancos de dados, redes e muito mais.

**Serviços Comuns:**
- **Azure Blob Storage:** Armazenamento de objetos escalável, ideal para dados brutos, backups e arquivos estáticos.
- **Azure Virtual Machines (VMs):** Permitem criar e gerenciar máquinas virtuais Windows ou Linux na nuvem.
- **Azure SQL Database:** Banco de dados relacional gerenciado com alta disponibilidade, escalabilidade e compatibilidade com SQL Server.

**Documentação e Suporte:**
- O Azure oferece documentação abrangente, tutoriais e suporte direto no portal. Acesse a documentação para obter detalhes sobre cada serviço.

## 7. Visão Geral dos Produtos Azure

1. **Explorando Todos os Serviços:**
   - No portal do Azure, clique em “All services” para explorar as diversas categorias, como Computação, Armazenamento, Banco de Dados, Rede e Inteligência Artificial.

2. **Azure Virtual Machines:**
   - **Visão Geral:** Serviço que permite criar instâncias de servidores virtuais sob demanda.
   - **Tipos de VMs:** Máquinas de uso geral, otimizadas para memória, computação, GPU, etc.
   - **Democratização:** A cloud democratiza o acesso a tecnologias antes complexas ou caras.

3. **Visão Geral de Vários Tipos de Banco de Dados:**
   - **Azure SQL Database:** Banco de dados relacional gerenciado.
   - **Azure Cosmos DB:** Banco de dados NoSQL globalmente distribuído.
   - **Azure Synapse Analytics:** Plataforma unificada para análise em grande escala.
   
   **Motivação para Estudo:** A diversidade de bancos de dados e serviços incentiva a aprender novas tecnologias e arquiteturas.

## 8. Tipos de Serviço no Azure

1. **Conta Gratuita (Free Account):**
   - **$200 de Crédito Inicial:** Geralmente oferecido para novos cadastros.
   - **Serviços Gratuitos por 12 Meses:** Alguns serviços permanecem gratuitos por um ano com limites específicos.
   - **Trial Limitado:** Após o crédito inicial, alguns serviços podem ter um período de teste limitado.

## 9. Configuração de Regiões no Azure

**Regiões e Zonas de Disponibilidade:**
- **Regiões** são localizações geográficas onde a Microsoft mantém data centers. Cada região pode ter múltiplas Zonas de Disponibilidade, que são locais fisicamente separados para alta disponibilidade.
- A escolha da região influencia na latência, requisitos legais e conformidade.

**Escolha da Região:**
- Selecione a região mais próxima dos usuários ou que atenda requisitos de compliance.
- Você pode facilmente alternar regiões ao criar recursos no portal do Azure.

## 10. Configuração de Identidade e Acesso (Azure Active Directory e RBAC)

**Importância do Azure AD e RBAC:**
- O Azure Active Directory (Azure AD) gerencia identidades e autenticação.
- O RBAC (Role-Based Access Control) permite atribuir permissões específicas a usuários, grupos e aplicativos.

**Criar um Fator de Autenticação Multifator (MFA):**
- Acesse o Azure AD no portal.
- Vá em “Users” e habilite MFA para sua conta, adicionando uma camada extra de segurança.

**Criar um Usuário com Permissões de Administrador:**
- Em Azure AD, crie um novo usuário.
- Atribua a ele uma função de administrador (por exemplo, "Owner" ou "Contributor" em um determinado recurso).
- Utilize tags, descrições e nomes claros para identificar e gerenciar o usuário.

## 11. Criando o Nosso Primeiro Serviço de Armazenamento (Blob Storage)

Aqui, aprenderemos a criar uma conta de armazenamento, configurar um container, fazer upload de arquivos e servir um site estático usando o Azure Blob Storage.

### 11.1 Criando uma Conta de Armazenamento

1. **Nome da Conta de Armazenamento:**
   - Escolha um nome globalmente único.
  
2. **Região:**
   - Selecione a região mais próxima do seu público-alvo.

3. **Redundância e Configurações:**
   - Defina o tipo de redundância (LRS, ZRS, GRS) e outras configurações iniciais.

4. **Acesso e Segurança:**
   - Por padrão, mantenha o acesso privado. Você pode ajustar posteriormente as permissões.

5. **Tags e Criptografia:**
   - Adicione tags para organização e habilite criptografia padrão.

### 11.2 Criando um Container no Blob Storage

- Dentro da conta de armazenamento, crie um container (por exemplo, “imagens”).
- Por padrão, mantenha o container privado.

### 11.3 Fazendo Upload de um Arquivo (Imagem)

1. **Upload:**
   - Carregue uma imagem pelo portal.
  
2. **Verificação do Arquivo:**
   - O arquivo não será público por padrão. Você não conseguirá acessá-lo via URL pública sem ajustes.

### 11.4 Configurando Permissões: Tornando um Blob Público

1. **Padrão Privado:**
   - Todos os blobs são privados inicialmente.
  
2. **Tornar o Blob Público:**
   - Ajuste o nível de acesso do container ou configure uma assinatura de acesso compartilhado (SAS) para permitir acesso público ou temporário.

### 11.5 Habilitando um Site Estático com Blob Storage

- Em “Static website” (nas configurações da conta de armazenamento), habilite a opção de website estático.
- Defina o `index.html` como página principal.

### 11.6 Adicionando `index.html`

- Faça upload do `index.html` para o container $web (criado automaticamente ao habilitar o site estático).

### 11.7 Acessando o Site Estático

- Após a configuração, acesse a URL fornecida para o site estático do Blob Storage.

### 11.8 Redirecionando para o `index.html`

- O serviço estático já serve o `index.html` na raiz, não sendo necessário redirecionamento manual, a não ser que você queira configurar páginas adicionais.

### 11.9 O que é um Site Estático?

- Um site estático é um conjunto de páginas HTML, CSS e JavaScript servidas diretamente, sem processamento dinâmico no servidor. Ideal para sites institucionais, portfólios ou páginas informativas.

## 12. Criando e Configurando uma Máquina Virtual (VM) no Azure

Vamos criar uma VM, acessar via SSH, configurar acesso root (no caso de distribuições Linux), instalar Python e Streamlit, e rodar um pequeno aplicativo web estático, incluindo a exibição de uma imagem hospedada no Blob Storage.

### 12.1 Criando a VM

1. **Azure Portal:**
   - Vá em “Virtual Machines” e clique em “Create”.
   - Escolha a imagem (Linux, por exemplo Ubuntu), tamanho da VM, usuário, SSH key ou senha.
   - Defina a região e o grupo de recursos.

2. **Configurar Rede e Segurança:**
   - Crie ou selecione uma Virtual Network.
   - Defina a NSG (Network Security Group) para permitir tráfego HTTP (porta 80) e SSH (porta 22).

### 12.2 Conectando-se à VM via SSH

1. **Conexão SSH:**
   - No terminal local, use:

   ```bash
   ssh -i "caminho-para-sua-chave.pem" azureuser@ip-publico-da-vm
   ```

2. **Acesso Root:**
   - Caso necessário, use `sudo su` para obter privilégios de administrador.

3. **Definir uma Senha Root (opcional):**
   ```bash
   sudo passwd root
   ```

### 12.3 Instalando Python, pip e Streamlit

1. **Atualizar Pacotes e Instalar Python3:**
   ```bash
   sudo apt-get update -y
   sudo apt-get install python3 -y
   ```

2. **Instalando pip3:**
   ```bash
   sudo apt-get install python3-pip -y
   ```

3. **Instalando Streamlit:**
   ```bash
   pip3 install streamlit
   ```

### 12.4 Criando o Código do Streamlit

1. **Criar o Arquivo `app.py`:**
   ```bash
   nano app.py
   ```

2. **Inserir o Código:**
   ```python
   import streamlit as st

   st.title("Hello, World!")
   st.write("Este é um simples aplicativo Streamlit rodando em uma VM no Azure.")
   ```

   - Salve e saia do nano: `Ctrl + O`, `Enter`, `Ctrl + X`.

### 12.5 Executando o Streamlit na Porta 80

1. **Executar:**
   ```bash
   sudo streamlit run app.py --server.port 80 --server.enableCORS false
   ```
   
2. **Acessar a Aplicação:**
   - No navegador, acesse o IP público da VM:
     ```http
     http://ip-publico-da-vm
     ```

### Resultado Esperado

Ao acessar o aplicativo, você verá o título "Hello, World!" e uma breve descrição. Com configurações adicionais, é possível carregar e exibir uma imagem do Blob Storage, simulando um fluxo semelhante ao do AWS S3, agora no contexto do Azure.
