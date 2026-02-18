# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE gold.customer_metrics (
# MAGIC     signup_date DATE,
# MAGIC     total_customers INT,
# MAGIC     created_at TIMESTAMP
# MAGIC );
