# 🍪 Guia Prático do Aluno · Fatec Taquaritinga
### Workshop: "Do cookie ao dashboard: Databricks & Carreira"
**Palestrante:** Vitor Hugo Nascimento · Lead Data Engineer & Technical Mentor  
**Repositório Oficial:** [palestra_factectq_databricks](https://github.com/vitorh-nascimento/palestra_factectq_databricks)

---

## 🎯 Objetivo
Este guia foi feito para você, estudante da Fatec Taquaritinga, que quer dar os primeiros passos práticos na área de dados sem gastar um centavo e sem precisar de um computador potente.

Tudo o que vimos na palestra roda 100% no navegador via **Databricks Free Edition**.

---

## 🛠️ Passo 1: Criando sua Conta Gratuita no Databricks
1. Acesse: **[signup.databricks.com](https://signup.databricks.com)**.
2. Preencha seu nome, e-mail e empresa/instituição (pode colocar `Fatec Taquaritinga`).
3. Na tela de seleção de plano, escolha **Databricks Free Edition**:
   * ✅ Não pede cartão de crédito.
   * ✅ Não expira.
   * ✅ Vem com clusters serverless e o dataset oficial da demo pré-instalado.

---

## 📍 Passo 2: Localizando o Dataset da Demo
No menu lateral esquerdo do Databricks:
1. Clique no ícone de banco de dados: **Catalog** (Unity Catalog).
2. Expanda o catálogo **`samples`**.
3. Expanda o schema **`bakehouse`**.
4. Você verá as tabelas da nossa rede de confeitarias:
   * `sales_transactions`: Histórico de vendas individuais.
   * `sales_customers`: Cadastro de clientes.
   * `sales_franchises`: Lojas espalhadas pelo mundo.
   * `sales_suppliers`: Fornecedores de insumos.
   * `media_customer_reviews`: Avaliações em texto livre dos clientes.
   * `media_gold_reviews_chunked`: As avaliações divididas em trechos (*chunks*), prontas para uso com IA.

---

## 🕵️‍♂️ Passo 3: Os Casos do CSI Cookie para Refazer

Abra um novo **Notebook** ou o **SQL Editor** e teste as queries abaixo:

### 1. Inventário Geral (Volumetria)
```sql
SELECT 'vendas' AS tabela, COUNT(*) AS linhas FROM samples.bakehouse.sales_transactions 
UNION ALL 
SELECT 'clientes', COUNT(*) FROM samples.bakehouse.sales_customers 
UNION ALL 
SELECT 'franquias', COUNT(*) FROM samples.bakehouse.sales_franchises;
```
> **Lição:** Sempre meça o tamanho das tabelas antes de começar a processar para planejar custo e performance.

---

### 2. Padrão de Vendas por Hora (Dado Sintético)
```sql
SELECT 
    HOUR(dateTime) AS hora, 
    COUNT(*) AS vendas 
FROM samples.bakehouse.sales_transactions 
GROUP BY hora 
ORDER BY hora;
```
*Transforme a tabela em **gráfico de barras** clicando em `+` > `Visualization`.*
> **Lição:** Vendas iguais às 3h da manhã e ao meio-dia? Desconfie do dado. Dados sintéticos costumam ser uniformes demais.

---

### 3. A Falsa Queda de Vendas do Dia 17 (Janela de Carga)
```sql
-- 1. Vendas por dia
SELECT DATE(dateTime) AS dia, COUNT(*) AS vendas 
FROM samples.bakehouse.sales_transactions 
GROUP BY dia ORDER BY dia;

-- 2. Limites do período
SELECT MIN(dateTime) AS inicio, MAX(dateTime) AS fim 
FROM samples.bakehouse.sales_transactions;
```
> **Lição:** As vendas do dia 17 param às 11h48. A ingestão foi parcial. Nunca apresente conclusões sem checar o corte temporal.

---

### 4. A Franquia Campeã (O Poder do JOIN)
```sql
SELECT 
    f.name AS franquia, 
    f.city AS cidade, 
    f.country AS pais, 
    ROUND(SUM(t.totalPrice), 2) AS faturamento 
FROM samples.bakehouse.sales_transactions t 
JOIN samples.bakehouse.sales_franchises f 
  ON t.franchiseID = f.franchiseID 
GROUP BY f.name, f.city, f.country 
ORDER BY faturamento DESC 
LIMIT 5;
```
> **Lição:** A tabela de vendas não tem a cidade; a tabela de lojas não tem as vendas. O `JOIN` é a cola do mundo relacional.

---

### 5. Perguntando em Português (Genie)
No menu lateral, abra o **Genie**, crie um espaço com as tabelas `sales_transactions` e `sales_franchises` e pergunte: *"Qual franquia vendeu mais?"*. Clique em **Show code** e compare o SQL gerado com o Caso 4.
> **Lição:** A IA acelera, mas quem entende o dado é quem confere se ela acertou.

---

### 🎁 Bônus: IA Generativa com SQL (AI Functions)
```sql
SELECT 
    review, 
    ai_analyze_sentiment(review) AS sentimento 
FROM samples.bakehouse.media_customer_reviews 
LIMIT 10;
```
> **Lição:** Você não precisa de uma biblioteca pesada de machine learning para classificar texto. O Lakehouse já traz funções de IA embutidas no SQL.

---

## 🏆 Desafio Extra para seu Portfólio (Vale Post no LinkedIn!)

Quer chamar a atenção de recrutadores para o seu primeiro estágio? Faça este projeto:
1. Descubra **qual dia da semana** tem maior volume de vendas usando a função `DAYOFWEEK(dateTime)`.
2. Identifique qual **sabor de biscoito** (`product`) gera o maior ticket médio (`AVG(totalPrice)`).
3. Tire print do seu notebook rodando no Databricks, suba o código no seu GitHub e poste no LinkedIn marcando a Fatec Taquaritinga, a Programmers e me marcando!

---

## 📚 Onde Continuar Estudando de Graça
* **Databricks Academy:** [databricks.com/learn/training](https://www.databricks.com/learn/training) — Cursos oficiais 100% gratuitos para estudantes.
* **Certificações Alvo:**
  * *Databricks Certified Data Analyst Associate*
  * *Databricks Certified Data Engineer Associate*
* **Treino Prático de SQL:** [SQLBolt (sqlbolt.com)](https://sqlbolt.com/) — Exercícios interativos rápidos no navegador.

