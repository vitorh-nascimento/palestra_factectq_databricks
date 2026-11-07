-- Quiz Relâmpago (alinhado ao deck) · gabarito nos comentários

-- Pergunta 1: Qual camada é o cookie embalado na prateleira? (Bronze / Silver / Gold)
-- Resposta: Gold (dado pronto para consumo)

-- Pergunta 2: Em que cidade fica a franquia campeã? (Nova York / Roma / Estocolmo)
-- Resposta: Roma (comprovação abaixo, mesma lógica do Caso 4)
SELECT
    f.name AS franquia,
    f.city AS cidade,
    ROUND(SUM(t.totalPrice), 2) AS faturamento_total
FROM samples.bakehouse.sales_transactions t
JOIN samples.bakehouse.sales_franchises f
  ON t.franchiseID = f.franchiseID
GROUP BY f.name, f.city
ORDER BY faturamento_total DESC
LIMIT 1;

-- Pergunta 3: Qual comando juntou vendas e franquias? (SELECT / JOIN / DELETE)
-- Resposta: JOIN

-- Pergunta 4: Por que as vendas "caíram" no dia 17?
-- Resposta: os dados param às 11h48 (a carga termina no meio do dia; comprovação abaixo, mesma lógica do Caso 3)
SELECT
    MIN(dateTime) AS primeira_venda_registrada,
    MAX(dateTime) AS ultima_venda_registrada
FROM samples.bakehouse.sales_transactions;

-- Pergunta 5: Qual coluna dá processo pela LGPD? (cidade / e-mail / sabor)
-- Resposta: e-mail (email_address é dado pessoal identificável)

-- Pergunta 6: Qual é a lição nº 1 da área de dados?
-- Resposta: desconfiar do dado


-- ============================================================
-- Desafio extra para casa
-- ============================================================

-- Desafio 1: Qual cookie vendeu mais unidades?
-- Resposta: Golden Gate Ginger (3.865 unidades)
SELECT 
    product, 
    SUM(quantity) AS total_unidades 
FROM samples.bakehouse.sales_transactions 
GROUP BY product 
ORDER BY total_unidades DESC 
LIMIT 1;

-- Desafio 2: Qual bandeira de cartão mais apareceu nas transações?
-- Resposta: Mastercard (1.144 vendas)
SELECT 
    paymentMethod, 
    COUNT(*) AS total_transacoes 
FROM samples.bakehouse.sales_transactions 
GROUP BY paymentMethod 
ORDER BY total_transacoes DESC;

