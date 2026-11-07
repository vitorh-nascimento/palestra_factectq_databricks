-- Caso 3: O mistério do dia 17
-- 3.1 Vendas agregadas por data
SELECT 
    DATE(dateTime) AS dia, 
    COUNT(*) AS vendas 
FROM samples.bakehouse.sales_transactions 
GROUP BY dia 
ORDER BY dia;

-- 3.2 Checagem da janela de carga / limites de corte temporal
SELECT 
    MIN(dateTime) AS primeira_venda, 
    MAX(dateTime) AS ultima_venda 
FROM samples.bakehouse.sales_transactions;

