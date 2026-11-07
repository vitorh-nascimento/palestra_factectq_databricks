-- Caso 4: A franquia campeã
-- Relacionamento via JOIN entre tabela de fatos e dimensões cadastrais
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

