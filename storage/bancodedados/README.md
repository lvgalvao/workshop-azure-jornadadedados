### **Azure SQL Database**

**Objetivo**: Nesta aula, vamos explorar o **Azure SQL Database**, suas principais funcionalidades, tipos de bancos de dados suportados, e aprender a configurar, gerenciar e otimizar bancos de dados na Microsoft Azure, comparando suas capacidades com o Amazon RDS.

---

### **1. O Que é o Azure SQL Database?**

- **Definição**: O Azure SQL Database é um serviço gerenciado de banco de dados relacional na nuvem, que oferece alta disponibilidade, escalabilidade e segurança. Ele suporta o mecanismo SQL Server, sendo ideal para aplicações críticas que exigem confiabilidade e desempenho.

- **Benefícios**:
  - **Gerenciamento Automatizado**: Tarefas como backups, atualizações e recuperação são automatizadas.
  - **Escalabilidade Flexível**: Permite escalar dinamicamente o desempenho do banco de dados com base na demanda.
  - **Segurança Integrada**: Oferece criptografia de dados em repouso e em trânsito, além de firewalls e autenticação multifator.
  - **Alta Disponibilidade**: Inclui redundância integrada e replicação geográfica opcional para garantir a continuidade dos negócios.

---

### **2. Principais Funcionalidades do Azure SQL Database**

#### **Alta Disponibilidade com Failover Automático**

- **O que é?**: O Azure SQL Database utiliza réplicas automáticas em diferentes data centers para garantir continuidade em caso de falhas.
- **Benefícios**:
  - **Failover Transparente**: Reduz o impacto de falhas no serviço, com mudanças automáticas entre réplicas.
  - **Opções de Replicação Geográfica**: Permite réplicas em regiões diferentes para maior proteção.

#### **Elastic Pools**

- **O que são?**: Elastic Pools permitem compartilhar recursos de computação entre múltiplos bancos de dados no mesmo servidor lógico, otimizando custos.
- **Uso Comum**:
  - Ideal para aplicações SaaS que hospedam vários clientes.
  - Permite alocação dinâmica de recursos para lidar com picos de demanda.

#### **Backup e Recuperação**

- **Backups Automáticos**:
  - Realiza backups automáticos com retenção de até 35 dias.
- **Restaurar para um Ponto no Tempo**:
  - Facilita a restauração do banco de dados para um momento específico, útil em casos de falhas ou erros humanos.

#### **Segurança e Monitoramento no Azure SQL Database**

- **Criptografia**:
  - Dados são criptografados com **Transparent Data Encryption (TDE)** e podem ser gerenciados pelo Azure Key Vault.
- **Firewall e Acesso Seguro**:
  - Permite configurar regras de firewall para restringir conexões apenas a IPs autorizados.
- **Monitoramento com Azure Monitor**:
  - Acompanhamento em tempo real de métricas como desempenho de consultas e uso de recursos.

---

### **3. Configurando o Azure SQL Database: Passo a Passo**

#### **1. Criando um Banco de Dados no Azure**

1. **Acessar o Portal do Azure**:
   - Faça login no **Azure Portal** e procure por **SQL Database**.
   - Clique em **"Create"** para iniciar o processo.

2. **Configurar o Banco de Dados**:
   - **Resource Group**: Selecione ou crie um grupo de recursos.
   - **Database Name**: Escolha um nome, como `BitcoinDB`.
   - **Server**: Configure um servidor lógico ou crie um novo, definindo login e senha de administrador.

3. **Escolher o Nível de Serviço**:
   - **Basic**: Para testes e desenvolvimento.
   - **Standard**: Para cargas de trabalho leves e médias.
   - **Premium**: Para aplicações críticas com alta demanda.

4. **Configurar a Conectividade**:
   - **Firewall**: Configure regras de firewall para permitir acesso ao banco de dados.
   - **Redes Virtuais**: Opção de integrar o banco em uma VNet para maior segurança.

5. **Finalizar Configuração**:
   - Revise os detalhes e clique em **"Create"**.

#### **2. Gerenciando o Banco de Dados com o SQL Editor Online**

1. Acesse o SQL Database no portal.
2. Clique em **"Query Editor"**.
3. Insira as credenciais de administrador e execute comandos diretamente pelo navegador.

#### **3. Criando a Tabela da Aplicação**

Usando o editor SQL online, crie a tabela do banco:

```sql
CREATE TABLE BitcoinData (
    id INT IDENTITY(1,1) PRIMARY KEY,
    valor FLOAT NOT NULL,
    criptomoeda NVARCHAR(10) NOT NULL,
    moeda NVARCHAR(10) NOT NULL,
    timestamp DATETIME NOT NULL
);
```

---

### **4. Comparação: Azure SQL Database vs Amazon RDS**

| **Critério**               | **Azure SQL Database**                                          | **Amazon RDS**                                           |
|----------------------------|---------------------------------------------------------------|---------------------------------------------------------|
| **Tipo de Banco Suportado** | SQL Server                                                   | MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Aurora |
| **Gerenciamento**           | Totalmente gerenciado com funcionalidades exclusivas do SQL Server | Gerenciado com suporte a múltiplos motores de banco   |
| **Elasticidade**            | Elastic Pools para compartilhar recursos                     | Read Replicas para escalabilidade de leitura           |
| **Alta Disponibilidade**    | Replicação automática e failover transparente                 | Multi-AZ e Read Replicas                                |
| **Interface de Gerenciamento** | Portal Azure e SQL Online Editor                             | AWS Console e ferramentas de terceiros                 |

---

### **5. Melhores Práticas com Azure SQL Database**

- **Segurança**: Sempre configure regras de firewall e habilite autenticação multifator para administradores.
- **Monitoramento Proativo**: Use o **Azure Monitor** para identificar gargalos de desempenho.
- **Backup e Recuperação**: Teste frequentemente a funcionalidade de restauração.
- **Escalabilidade Inteligente**: Utilize Elastic Pools para economizar recursos em ambientes multi-tenant.

---

Essa aula oferece uma visão completa sobre o gerenciamento de bancos de dados no Azure com o SQL Database, destacando suas vantagens e comparando com o Amazon RDS, preparando você para decisões estratégicas no uso da nuvem.

---

### **Inserindo Dados na Tabela**

```sql
-- Inserindo registros de exemplo na tabela BitcoinData
INSERT INTO BitcoinData (valor, criptomoeda, moeda, timestamp)
VALUES 
(26250.45, 'BTC', 'USD', '2024-12-20 14:35:00'),
(18500.30, 'BTC', 'EUR', '2024-12-20 15:00:00'),
(1500.75, 'ETH', 'USD', '2024-12-20 16:00:00'),
(1600.10, 'ETH', 'EUR', '2024-12-20 17:15:00'),
(30000.00, 'BTC', 'BRL', '2024-12-20 18:00:00');
```

---

### **Consultas Simples**

#### 1. Selecionar todos os registros:
```sql
SELECT * FROM BitcoinData;
```

#### 2. Filtrar registros por criptomoeda:
```sql
SELECT * FROM BitcoinData
WHERE criptomoeda = 'BTC';
```

#### 3. Filtrar por uma faixa de valores:
```sql
SELECT * FROM BitcoinData
WHERE valor BETWEEN 1500 AND 20000;
```

#### 4. Ordenar os resultados por valor:
```sql
SELECT * FROM BitcoinData
ORDER BY valor DESC;
```

#### 5. Agrupar por criptomoeda e calcular média dos valores:
```sql
SELECT criptomoeda, AVG(valor) AS media_valor
FROM BitcoinData
GROUP BY criptomoeda;
```

---

### **Consultas Mais Avançadas**

#### 6. Selecionar os 3 valores mais altos para BTC:
```sql
SELECT TOP 3 valor, timestamp
FROM BitcoinData
WHERE criptomoeda = 'BTC'
ORDER BY valor DESC;
```

#### 7. Contar o número de registros por moeda:
```sql
SELECT moeda, COUNT(*) AS total_transacoes
FROM BitcoinData
GROUP BY moeda;
```

#### 8. Encontrar o maior valor por criptomoeda:
```sql
SELECT criptomoeda, MAX(valor) AS maior_valor
FROM BitcoinData
GROUP BY criptomoeda;
```

#### 9. Filtrar registros por data e hora:
```sql
SELECT *
FROM BitcoinData
WHERE timestamp >= '2024-12-20 15:00:00'
  AND timestamp <= '2024-12-20 18:00:00';
```
---

Esses exemplos cobrem operações básicas e avançadas com a tabela `BitcoinData`, ajudando tanto em análises simples quanto em consultas mais detalhadas. Caso precise de algo específico, posso elaborar!