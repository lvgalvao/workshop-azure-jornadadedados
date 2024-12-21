## ETL Extração API usando Azure VMs

### Contexto de Aprendizado
Este guia demonstra como desenvolver e implantar uma ETL de Extração via API utilizando Azure VMs. O projeto inclui:

1. **ETL de Extração API** executando a cada 15 segundos.

### Inicializar o Projeto

#### 1. Acessar o Serviço de Virtual Machines no Azure

- Navegue até o portal do Azure.
- Selecione **Virtual Machines** no menu de serviços.
- Escolha a VM que você deseja configurar ou crie uma nova conforme necessário.

#### 2. Acessar a VM via SSH

Use o seguinte comando no seu terminal para conectar-se à VM. Certifique-se de substituir `<your-private-key>.pem` pelo caminho da sua chave privada e `<seu-ip-publico>` pelo endereço IP público da sua VM.

```bash
ssh -i ~/.ssh/<your-private-key>.pem azureuser@<seu-ip-publico>
```

*Exemplo:*
```bash
ssh -i ~/.ssh/id_rsa.pem azureuser@123.45.67.89
```

#### 3. Atualizar a Máquina

Atualize os pacotes existentes para garantir que todos os softwares estejam na versão mais recente.

```bash
sudo apt update
sudo apt upgrade -y
```

#### 4. Instalar Dependências Necessárias

Instale pacotes que permitem ao `apt` usar repositórios via HTTPS.

```bash
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
```

#### 5. Clonar o Repositório do Projeto

Clone o repositório Git que contém o seu projeto ETL.

```bash
git clone https://github.com/lvgalvao/ETLProjectAPIExtractAOVIVO.git
cd ETLProjectAPIExtractAOVIVO
```

#### 6. Instalar o Docker

##### a. Adicionar a Chave Oficial do Docker

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

##### b. Configurar o Repositório do Docker

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

##### c. Atualizar os Repositórios e Instalar o Docker

```bash
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
```

#### 7. Verificar a Instalação do Docker

Após reiniciar, reconecte-se via SSH e execute:

Este comando verifica se o Docker foi instalado corretamente exibindo uma mensagem de confirmação.

#### 8. Configurar Permissões de Usuário (Opcional)

Para evitar a necessidade de usar `sudo` com comandos Docker, adicione seu usuário ao grupo `docker`.

```bash
sudo usermod -aG docker $USER
```

Reinicie a VM para garantir que todas as alterações entrem em vigor.

```bash
sudo reboot
```

```bash
docker run hello-world
```

Depois, faça logout e login novamente ou reinicie a sessão SSH para que as alterações tenham efeito.

#### 9. Executar o Projeto com Docker Compose (Recomendado)

Para facilitar a execução de múltiplos serviços (ETL, Dashboard e PostgreSQL), é recomendável usar o Docker Compose. Certifique-se de que o `docker-compose.yml` está presente no repositório clonado.

##### a. Instalar o Docker Compose

Verifique a versão mais recente do Docker Compose [aqui](https://docs.docker.com/compose/install/). Por exemplo, para instalar a versão 2:

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Verifique a instalação:

```bash
docker-compose --version
```

##### b. Construir e Rodar os Contêineres

No diretório raiz do projeto (onde está o `docker-compose.yml`), execute:

```bash
touch .env
```

```
vi .env
```

```bash
docker-compose up -d
```

Este comando irá construir as imagens (se necessário) e iniciar os contêineres em segundo plano.

##### c. Verificar os Contêineres em Execução

```bash
docker-compose ps
```