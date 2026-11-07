# Databricks notebook source
# MAGIC %md
# MAGIC # CSI Cookie: Investigando a Bakehouse no Databricks
# MAGIC **Palestra:** Do cookie ao dashboard: Databricks & Carreira  
# MAGIC **Palestrante:** Vitor Hugo Nascimento (Lead Data Engineer & Technical Mentor)  
# MAGIC **Instituição:** Fatec Taquaritinga · 11/11/2026  
# MAGIC **Catálogo / Schema:** `samples.bakehouse`

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🕵️‍♂️ Caso 1: Quanta coisa tem aqui? (Volumetria)
# MAGIC **Pergunta para a plateia:** Qual dessas tabelas vocês acham que é a maior da rede?

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Caso 1: Inventário de linhas das tabelas principais
# MAGIC SELECT 'vendas' AS tabela, COUNT(*) AS linhas FROM samples.bakehouse.sales_transactions 
# MAGIC UNION ALL 
# MAGIC SELECT 'clientes', COUNT(*) FROM samples.bakehouse.sales_customers 
# MAGIC UNION ALL 
# MAGIC SELECT 'franquias', COUNT(*) FROM samples.bakehouse.sales_franchises 
# MAGIC UNION ALL
# MAGIC SELECT 'fornecedores', COUNT(*) FROM samples.bakehouse.sales_suppliers;

# COMMAND ----------

# MAGIC %md
# MAGIC ## ⏰ Caso 2: Que horas o povo come cookie? (Análise Temporal)
# MAGIC **Pergunta para a plateia:** Manhã, almoço ou noite?  
# MAGIC *Dica:* Alterne para visualização em **Gráfico de Barras** (X = `hora`, Y = `vendas`).

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Caso 2: Vendas distribuídas por hora do dia
# MAGIC SELECT 
# MAGIC     HOUR(dateTime) AS hora, 
# MAGIC     COUNT(*) AS vendas 
# MAGIC FROM samples.bakehouse.sales_transactions 
# MAGIC GROUP BY hora 
# MAGIC ORDER BY hora;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🔎 Caso 3: O mistério do dia 17 (Janela de Carga)
# MAGIC **Pergunta para a plateia:** Em 17/05/2024 as vendas caíram pela metade. A padaria pegou fogo?

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Caso 3.1: Vendas por dia
# MAGIC SELECT 
# MAGIC     DATE(dateTime) AS dia, 
# MAGIC     COUNT(*) AS vendas 
# MAGIC FROM samples.bakehouse.sales_transactions 
# MAGIC GROUP BY dia 
# MAGIC ORDER BY dia;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Caso 3.2: O que aconteceu no dia 17? Conferindo início e fim da janela de dados
# MAGIC SELECT 
# MAGIC     MIN(dateTime) AS primeira_venda_registrada, 
# MAGIC     MAX(dateTime) AS ultima_venda_registrada 
# MAGIC FROM samples.bakehouse.sales_transactions;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🏆 Caso 4: A franquia campeã (O Primeiro JOIN)
# MAGIC **Pergunta para a plateia:** Em qual país fica a franquia que mais faturou?

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Caso 4: Faturamento por franquia e localização
# MAGIC SELECT 
# MAGIC     f.name AS franquia, 
# MAGIC     f.city AS cidade, 
# MAGIC     f.country AS pais, 
# MAGIC     ROUND(SUM(t.totalPrice), 2) AS faturamento_total 
# MAGIC FROM samples.bakehouse.sales_transactions t 
# MAGIC JOIN samples.bakehouse.sales_franchises f 
# MAGIC   ON t.franchiseID = f.franchiseID 
# MAGIC GROUP BY f.name, f.city, f.country 
# MAGIC ORDER BY faturamento_total DESC 
# MAGIC LIMIT 5;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🔒 Caso 5: O vazamento (Governança & LGPD no Unity Catalog)
# MAGIC **Pergunta para a plateia:** Se esse banco vazasse amanhã, qual coluna daria processo?

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Caso 5.1: Inspecionando colunas e tipos em clientes
# MAGIC DESCRIBE TABLE samples.bakehouse.sales_customers;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Caso 5.2: Inspecionando colunas e tipos em transações
# MAGIC DESCRIBE TABLE samples.bakehouse.sales_transactions;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Exemplo Conceitual de Mascaramento Dinâmico (Unity Catalog):
# MAGIC > ⚠️ **Nota Prática:** O catálogo `samples` é **somente leitura**. Para testar o mascaramento de dados (Dynamic Column Masking) de verdade, é preciso copiar a tabela para um catálogo próprio onde você tenha permissão de escrita e aplicar a máscara nela:
# MAGIC > ```sql
# MAGIC > CREATE TABLE main.default.clientes AS 
# MAGIC > SELECT * FROM samples.bakehouse.sales_customers;
# MAGIC > ```
# MAGIC
# MAGIC ```sql
# MAGIC -- Criando regra de mascaramento para LGPD:
# MAGIC CREATE OR REPLACE FUNCTION mascara_email(email STRING) 
# MAGIC RETURN CASE 
# MAGIC     WHEN is_account_group_member('rh_privilegiado') THEN email 
# MAGIC     ELSE CONCAT(SUBSTRING(email, 1, 2), '****@', SPLIT(email, '@')[1]) 
# MAGIC END;
# MAGIC
# MAGIC -- Aplicando na coluna sensível da tabela:
# MAGIC ALTER TABLE main.default.clientes 
# MAGIC ALTER COLUMN email_address SET MASK mascara_email;
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🤖 Caso 6: Perguntando em Português (Databricks Assistant / Genie)
# MAGIC **Prompt para testar ao vivo:** `"Qual franquia vendeu mais?"`

# COMMAND ----------

# MAGIC %sql
# MAGIC -- SQL de referência gerado pelo Assistant / Genie:
# MAGIC SELECT 
# MAGIC     f.name, 
# MAGIC     SUM(t.totalPrice) AS total 
# MAGIC FROM samples.bakehouse.sales_transactions t 
# MAGIC JOIN samples.bakehouse.sales_franchises f 
# MAGIC   ON t.franchiseID = f.franchiseID 
# MAGIC GROUP BY f.name 
# MAGIC ORDER BY total DESC 
# MAGIC LIMIT 1;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 💡 BÔNUS: IA dentro do Lakehouse (AI Functions)
# MAGIC Classificação de sentimentos em tempo de execução SQL sobre texto livre de clientes.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Bônus: Analisando avaliações dos clientes com GenAI nativa
# MAGIC SELECT 
# MAGIC     review, 
# MAGIC     ai_analyze_sentiment(review) AS sentimento 
# MAGIC FROM samples.bakehouse.media_customer_reviews 
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🍪 Quiz Relâmpago
# MAGIC 1. Qual camada é o cookie embalado na prateleira? (Bronze / Silver / Gold)
# MAGIC 2. Em que cidade fica a franquia campeã? (Nova York / Roma / Estocolmo)
# MAGIC 3. Qual comando juntou vendas e franquias? (SELECT / JOIN / DELETE)
# MAGIC 4. Por que as vendas "caíram" no dia 17?
# MAGIC 5. Qual coluna dá processo pela LGPD? (cidade / e-mail / sabor)
# MAGIC 6. Qual é a lição nº 1 da área de dados?

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Gabarito do Quiz Relâmpago:
# MAGIC -- 1) Gold (dado pronto para consumo)
# MAGIC -- 2) Roma (comprovação abaixo, mesma lógica do Caso 4)
# MAGIC -- 3) JOIN
# MAGIC -- 4) Os dados param às 11h48 (comprovação na célula seguinte, mesma lógica do Caso 3)
# MAGIC -- 5) e-mail (email_address é dado pessoal identificável)
# MAGIC -- 6) Desconfiar do dado
# MAGIC SELECT
# MAGIC     f.name AS franquia,
# MAGIC     f.city AS cidade,
# MAGIC     ROUND(SUM(t.totalPrice), 2) AS faturamento_total
# MAGIC FROM samples.bakehouse.sales_transactions t
# MAGIC JOIN samples.bakehouse.sales_franchises f
# MAGIC   ON t.franchiseID = f.franchiseID
# MAGIC GROUP BY f.name, f.city
# MAGIC ORDER BY faturamento_total DESC
# MAGIC LIMIT 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Quiz P4: até que horas vão os dados?
# MAGIC SELECT
# MAGIC     MIN(dateTime) AS primeira_venda_registrada,
# MAGIC     MAX(dateTime) AS ultima_venda_registrada
# MAGIC FROM samples.bakehouse.sales_transactions;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 🏠 Desafio extra para casa

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Desafio 1: Qual cookie vendeu mais unidades?
# MAGIC SELECT 
# MAGIC     product, 
# MAGIC     SUM(quantity) AS total_unidades 
# MAGIC FROM samples.bakehouse.sales_transactions 
# MAGIC GROUP BY product 
# MAGIC ORDER BY total_unidades DESC 
# MAGIC LIMIT 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Desafio 2: Qual bandeira de cartão mais apareceu?
# MAGIC SELECT 
# MAGIC     paymentMethod, 
# MAGIC     COUNT(*) AS total_transacoes 
# MAGIC FROM samples.bakehouse.sales_transactions 
# MAGIC GROUP BY paymentMethod 
# MAGIC ORDER BY total_transacoes DESC;

