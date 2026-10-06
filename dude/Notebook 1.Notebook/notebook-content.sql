-- Fabric notebook source

-- METADATA ********************

-- META {
-- META   "kernel_info": {
-- META     "name": "synapse_pyspark"
-- META   },
-- META   "dependencies": {
-- META     "lakehouse": {
-- META       "default_lakehouse": "8b02caa4-2cf4-4de3-bbe2-ed285f579b00",
-- META       "default_lakehouse_name": "axfabriclakehouse",
-- META       "default_lakehouse_workspace_id": "1589f8a3-9d2c-4aa7-98d2-4e6c2e5e92dc",
-- META       "known_lakehouses": [
-- META         {
-- META           "id": "8b02caa4-2cf4-4de3-bbe2-ed285f579b00"
-- META         }
-- META       ]
-- META     }
-- META   }
-- META }

-- CELL ********************

DROP TABLE IF EXISTS dummy_dim_customer;

CREATE TABLE dummy_dim_customer
USING DELTA
AS
SELECT *
FROM VALUES
    (1, 'Customer A', 'UAE'),
    (2, 'Customer B', 'UK'),
    (3, 'Customer C', 'India'),
    (4, 'Customer D', 'USA'),
    (5, 'Customer E', 'Singapore')
AS t(customer_id, customer_name, country);

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

DROP TABLE IF EXISTS dummy_dim_time;

CREATE TABLE dummy_dim_time
USING DELTA
AS
SELECT
    date_id,
    CAST(full_date AS DATE) AS full_date,
    year,
    month,
    day
FROM VALUES
    (20260101, '2026-01-01', 2026, 1, 1),
    (20260102, '2026-01-02', 2026, 1, 2),
    (20260103, '2026-01-03', 2026, 1, 3),
    (20260104, '2026-01-04', 2026, 1, 4),
    (20260105, '2026-01-05', 2026, 1, 5)
AS t(date_id, full_date, year, month, day);


-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

DROP TABLE IF EXISTS dummy_fact_sales;

CREATE TABLE dummy_fact_sales
USING DELTA
AS
SELECT *
FROM VALUES
    (1, 1, 20260101, 'Product A', 2, 100.00),
    (2, 2, 20260101, 'Product B', 1, 250.00),
    (3, 1, 20260102, 'Product C', 3, 75.00),
    (4, 3, 20260103, 'Product A', 5, 250.00),
    (5, 4, 20260104, 'Product D', 2, 400.00),
    (6, 5, 20260105, 'Product B', 4, 1000.00)
AS t(
    sale_id,
    customer_id,
    date_id,
    product_name,
    quantity,
    sales_amount
);

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }
