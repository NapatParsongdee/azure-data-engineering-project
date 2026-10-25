# Databricks notebook source
# MAGIC %md
# MAGIC #Create Catalog
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS store_catalog

# COMMAND ----------

# MAGIC %md
# MAGIC #Create Schema

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS store_catalog.bronze;
# MAGIC CREATE SCHEMA IF NOT EXISTS store_catalog.silver;
# MAGIC CREATE SCHEMA IF NOT EXISTS store_catalog.gold;