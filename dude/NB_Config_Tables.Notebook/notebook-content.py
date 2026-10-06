# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "8b02caa4-2cf4-4de3-bbe2-ed285f579b00",
# META       "default_lakehouse_name": "axfabriclakehouse",
# META       "default_lakehouse_workspace_id": "1589f8a3-9d2c-4aa7-98d2-4e6c2e5e92dc",
# META       "known_lakehouses": [
# META         {
# META           "id": "8b02caa4-2cf4-4de3-bbe2-ed285f579b00"
# META         }
# META       ]
# META     },
# META     "warehouse": {
# META       "known_warehouses": []
# META     }
# META   }
# META }

# CELL ********************

spark.sql("""
CREATE TABLE IF NOT EXISTS config.cfg_pipeline_settings (
    pipeline_id STRING, source_name STRING, environment STRING, base_url STRING,
    auth_type STRING, login_endpoint STRING, api_key_secret_name STRING,
    username_secret_name STRING, password_secret_name STRING, is_admin_flag BOOLEAN,
    verify_ssl BOOLEAN, timeout_seconds INT, raw_path STRING, silver_raw_path STRING,
    bronze_lakehouse_name STRING, write_mode STRING, audit_enabled BOOLEAN, audit_table STRING,
    token_cache_max_age_hours INT, full_login_max_age_hours INT, is_active BOOLEAN,
    created_date TIMESTAMP, modified_date TIMESTAMP
) USING DELTA
""")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("""

INSERT INTO config.cfg_pipeline_settings VALUES

 ('pl_xpedeon','xpedeon','dev','https://sobhaalsiniya-api.onxpedeon.com:9155',NULL,NULL,'xpedeon-api-key',NULL,NULL,NULL,false,600,'/lakehouse/default/Files','/lakehouse/default/Files','LH_Bronze','overwrite',true,'etl_audit',NULL,NULL,true,current_timestamp(),current_timestamp())

""")



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("""

CREATE TABLE IF NOT EXISTS config.cfg_table_extract (

    config_id STRING, pipeline_id STRING, table_name STRING, load_type STRING,

    incremental_column STRING, run_order INT, extract_params STRING,

    is_active BOOLEAN, first_load_done BOOLEAN, last_extracted_value STRING,

    last_run_status STRING, last_run_timestamp TIMESTAMP, last_row_count BIGINT,

    created_date TIMESTAMP, modified_date TIMESTAMP

) USING DELTA

""")



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import uuid

spark.sql(f"""

INSERT INTO config.cfg_table_extract VALUES

('{str(uuid.uuid4())}','pl_xpedeon','cm_cost_head','full',NULL,8,'{{"source_query": "SELECT * FROM cm_cost_head"}}',true,NULL,NULL,NULL,NULL,NULL,current_timestamp(),current_timestamp()),
('{str(uuid.uuid4())}','pl_xpedeon','cm_internal_entity','full',NULL,9,'{{"source_query": "SELECT * FROM cm_internal_entity"}}',true,NULL,NULL,NULL,NULL,NULL,current_timestamp(),current_timestamp()),
('{str(uuid.uuid4())}','pl_xpedeon','cm_cost_code','full',NULL,7,'{{"source_query": "SELECT * FROM cm_cost_code"}}',true,NULL,NULL,NULL,NULL,NULL,current_timestamp(),current_timestamp())

""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("""
UPDATE config.cfg_table_extract  

SET run_order = 3

WHERE table_name = 'cm_cost_code';
""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
