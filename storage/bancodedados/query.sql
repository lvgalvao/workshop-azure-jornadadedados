Aqui estão os exemplos de `INSERT INTO` e consultas para a tabela `BitcoinData`:

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

#### 10. Usar uma subquery para encontrar a moeda com maior número de transações:
```sql
SELECT moeda
FROM BitcoinData
GROUP BY moeda
ORDER BY COUNT(*) DESC
LIMIT 1;
```

---

Esses exemplos cobrem operações básicas e avançadas com a tabela `BitcoinData`, ajudando tanto em análises simples quanto em consultas mais detalhadas. Caso precise de algo específico, posso elaborar!