-- Caso 2: Que horas o povo come biscoito?
-- Análise de vendas agregadas por hora do dia (Demonstração de dado sintético / uniforme)
SELECT 
    HOUR(dateTime) AS hora, 
    COUNT(*) AS vendas 
FROM samples.bakehouse.sales_transactions 
GROUP BY hora 
ORDER BY hora;

