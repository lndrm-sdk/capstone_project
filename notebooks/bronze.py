# Databricks notebook source
catalog = dbutils.widgets.get("catalog")
print("Using catalog:", catalog)


# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE bronze.customer_raw (
# MAGIC     customer_id STRING,
# MAGIC     name STRING,
# MAGIC     email STRING,
# MAGIC     signup_date STRING,
# MAGIC     ingestion_timestamp TIMESTAMP
# MAGIC );
