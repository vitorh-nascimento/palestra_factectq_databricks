-- Caso 1: Quanta coisa tem aqui?
-- Inventário de linhas das tabelas do dataset samples.bakehouse
SELECT 'vendas' AS tabela, COUNT(*) AS linhas FROM samples.bakehouse.sales_transactions 
UNION ALL 
SELECT 'clientes', COUNT(*) FROM samples.bakehouse.sales_customers 
UNION ALL 
SELECT 'franquias', COUNT(*) FROM samples.bakehouse.sales_franchises 
UNION ALL
SELECT 'fornecedores', COUNT(*) FROM samples.bakehouse.sales_suppliers;

