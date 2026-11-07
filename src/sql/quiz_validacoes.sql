-- Queries de Validação e Gabarito do Quiz Relâmpago

-- Pergunta 3: Qual cookie vendeu mais unidades?
-- Resposta: Golden Gate Ginger (3.865 unidades)
SELECT 
    product, 
    SUM(quantity) AS total_unidades 
FROM samples.bakehouse.sales_transactions 
GROUP BY product 
ORDER BY total_unidades DESC 
LIMIT 1;

-- Pergunta 4: Qual bandeira de cartão mais apareceu nas transações?
-- Resposta: Mastercard (1.144 vendas)
SELECT 
    cardType, 
    COUNT(*) AS total_transacoes 
FROM samples.bakehouse.sales_transactions 
GROUP BY cardType 
ORDER BY total_transacoes DESC;

