# Azure-Data-Engineering-Project

## 📌 Project Overview
This project focuses on building a comprehensive data engineering pipeline using Azure Data Factory, Azure Databricks, and PySpark. It leverages modern cloud technologies and best practices to ensure efficient data processing and governance.

I will use unclean datasets from [DataWithBaraa's Databricks Bootcamp 2026](https://github.com/DataWithBaraa/databricks_bootcamp_2026/tree/main/datasets/engineering) to better demonstrate the data cleaning and transformation process.
  
![image](Picture/picture1.png)

---

## 🔑 Key Components
- **Azure Data Factory:** Orchestrates data workflows.
- **Databricks & PySpark:** Enables scalable data transformations.
- **Unity Catalog:** Implements data governance and access control.
- **Delta Lake & Delta Tables:** Provides efficient and reliable data storage.
- **Medallion Architecture:** Structures data pipelines into Bronze, Silver, and Gold layers.
- **Dimensional Data Modeling in Azure Databricks:** Designs and optimizes data warehouses.
- **Slowly Changing Dimensions (SCD):** Implements historical data tracking in Databricks.

---

## 🏗️ Architecture Overview
This project follows the **Medallion Architecture**:
1. **Bronze Layer:** Raw data ingestion from multiple sources.
2. **Silver Layer:** Cleansing and transformation of data.
3. **Gold Layer:** Business-ready, analytics-optimized data.

---

## 📂 Project Folder Structure

```
azure-data-engineering-project/
│
├── adf/
│   ├── pipelines/
│   ├── datasets/
│   └── linkedService/
│
├── databricks/
│   ├── bronze to silver transformations.py
│   ├── silver to gold transformations.py
│   └── storagemount.py
│
├── synapse/
│   ├── sql-scripts/
|   ├── pipelines/
│   ├── datasets/
│   └── linkedService/
│
├── powerbi/
│   └── Dashboard 1.pbix
│
├── screenshots/
│   ├── ADF Pipeline.png/
|   ├── Dashboard 1.png/
│   ├── Resource group.png/
│   └── Synapse pipeline.png/
│
└── README.md
```

---

## 🔄 Data Pipeline Details

### 1️⃣ Data Ingestion (ADF)

* Extracts data from github
* Uses Copy Activity
* Loads raw data into **Bronze layer** in ADLS Gen2

### 2️⃣ Bronze Layer

* Raw, unprocessed data
* Stored in original schema

### 3️⃣ Silver Layer (Databricks) 
(Note: The examples below illustrate some of the data transformation steps performed in the Silver Layer. Due to unclean datasets, there are too many transformations to list here.)
* Data cleansing
* Schema enforcement
* Data type corrections
* Deduplication

### 4️⃣ Gold Layer (Databricks)

* Business-level aggregations
* Analytical-ready datasets
* Optimized for reporting

---

## 🚀 How to Run This Project

### Prerequisites

* Azure Subscription
* SQL Server (on-premise or VM)
* Azure Data Factory
* Azure Databricks Workspace
* Azure Data Lake Storage Gen2

### Steps

1. Create Azure resources
2. Configure Linked Services in ADF
3. Run ADF pipelines
4. Execute Databricks notebooks (Bronze → Silver → Gold)

---

## 📸 Screenshots 

* ADF pipeline execution
* Synapse pipeline execution
* Power BI dashboard
* Resource group

(Added images inside a `/screenshots` folder)



