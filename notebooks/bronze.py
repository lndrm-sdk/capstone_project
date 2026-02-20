# Databricks notebook source
catalog = dbutils.widgets.get("catalog")
print("Using catalog:", catalog)


# COMMAND ----------

spark.sql("""
CREATE OR REPLACE TABLE bronze.customer_raw (
    customer_id STRING,
    name STRING,
    email STRING,
    signup_date STRING,
    ingestion_timestamp TIMESTAMP
)
""")
