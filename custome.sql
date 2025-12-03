

-- Query: read data from CUSTOMER table in Snowflake
-- Note: credentials were removed from this file. Do not store secrets in SQL files.

SELECT *
FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER
LIMIT 40;



SELECT COUNT(*) AS TOTAL_CUSTOMERS
FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER;