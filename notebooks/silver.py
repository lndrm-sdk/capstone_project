# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE silver.customer_clean (
# MAGIC     customer_id INT,
# MAGIC     name STRING,
# MAGIC     email STRING,
# MAGIC     signup_date DATE,
# MAGIC     created_at TIMESTAMP
# MAGIC );
