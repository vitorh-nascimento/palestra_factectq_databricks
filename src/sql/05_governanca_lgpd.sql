-- Caso 5: O vazamento (Governança e Proteção de Dados / LGPD)
DESCRIBE TABLE samples.bakehouse.sales_customers;
DESCRIBE TABLE samples.bakehouse.sales_transactions;

-- Nota: O catálogo samples é somente leitura. Para testar o mascaramento de verdade:
-- CREATE TABLE main.default.clientes AS SELECT * FROM samples.bakehouse.sales_customers;

-- Exemplo de máscara dinâmica no Unity Catalog:
-- CREATE OR REPLACE FUNCTION mascara_email(email STRING) 
-- RETURN CASE 
--     WHEN is_account_group_member('rh_privilegiado') THEN email 
--     ELSE CONCAT(SUBSTRING(email, 1, 2), '****@', SPLIT(email, '@')[1]) 
-- END;
--
-- ALTER TABLE main.default.clientes 
-- ALTER COLUMN email_address SET MASK mascara_email;
