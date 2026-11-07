-- Caso 5: O vazamento (Governança e Proteção de Dados / LGPD)
DESCRIBE TABLE samples.bakehouse.sales_customers;
DESCRIBE TABLE samples.bakehouse.sales_transactions;

-- Exemplo conceitual de mascara dinâmica no Unity Catalog:
-- ALTER TABLE samples.bakehouse.sales_customers 
-- ALTER COLUMN email_address SET MASK mascara_email;

