# Databricks notebook source
dbutils.widgets.text("catalog", "")
catalog = dbutils.widgets.get("catalog")

print("Using catalog:", catalog)

# Set Unity Catalog context
spark.sql(f"USE CATALOG {catalog}")

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
