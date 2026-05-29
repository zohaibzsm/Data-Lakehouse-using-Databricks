# 🏗️ Sales Data Lakehouse on Databricks
 
> A production-grade data lakehouse pipeline built on **Databricks**, implementing the **Medallion Architecture** across **Orders**, **Customers**, and **Products** domains. Engineered for reliability, scalability, and analytical performance using **Delta Lake**, **Apache Spark**, **Unity Catalog**, **SQL**,  and **Databricks Workflows**.

## 📌 Project Summary
 
Modern retailers generate high-volume transactional data across multiple domains — orders, customers, and products. This project engineers a **fully governed, layered lakehouse** on Databricks that takes raw operational data from ingestion to analytics-ready Gold tables via scheduled batch pipelines.
 
The architecture is designed around three core principles:
- **Reliability** — ACID-compliant Delta tables with schema enforcement at every layer
- **Governance** — Unity Catalog for centralised access control and data lineage
- **Auditability** — Delta time travel and pipeline run metadata preserved throughout

## 🏛️ Architecture
![Data Architecture](docs/data%20arcitecture.JPG)

The data architecture for this project follows Medallion Architecture: Bronze, Silver, and Gold layers.

### 🥉 Bronze — Raw Ingestion
Lands raw data **as-is** from source systems. No business logic is applied — this layer is the single source of truth for historical replay.

### 🥈 Silver — Cleansed & Conformed
Applies **data quality rules**, trimming, normalization, deduplication, type casting, and business-key resolution. The Silver layer is the trusted, queryable representation of operational data.

### 🥇 Gold — Analytics-Ready
Aggregated, denormalised tables purpose-built for BI and analytical consumption. Modelled for query performance, not storage efficiency.

## 📖 Project Overview

This project involves:

1. **Data Architecture**: Designing a Modern Data Lakehouse Using Medallion Architecture **Bronze**, **Silver**, and **Gold** layers.
2. **ETL Pipelines**: Extracting, transforming, and loading data from source systems into the lakehouse in Databricks.
3. **Data Modeling**: Developing fact and dimension tables optimized for analytical queries.

## 🚀 Project Requirements

### Building the Data Lakehouse (Data Engineering)

#### Objective
Develop a modern data lakehouse using PySpark and Spark SQL to consolidate sales data, enabling analytical reporting and informed decision-making.

#### Specifications
- **Data Sources**: Import data from two source systems (ERP and CRM) provided as CSV files.
- **Data Quality**: Cleanse and resolve data quality issues before analysis.
- **Integration**: Combine both sources into a single, user-friendly data model designed for analytical queries.
- **Scope**: Focus on the latest dataset only; historization of data is not required.
- **Documentation**: Provide clear documentation of the data model to support both business stakeholders and analytics teams.


## 📁 Repository Structure
 
```
Data-Lakehouse-using-Databricks/
│
├── scripts/
│   ├── bronze/
│   │   ├── load_bronze.ipynb    # raw ingestion for all sources from Unity Catalog volume to delta table
│   │   ├── bronze_config.py     # source configurations
│   │
│   ├── silver/
│   │   ├── CRM_cust_info.ipynb       # Customers
│   │   ├── CRM_prd_info.ipynb        # Products
│   │   └── CRM_sales_details.ipynb   # Sales details
│   │   ├── ERP_cust_az12.ipynb       # Customers related
│   │   ├── ERP_loc_a101.ipynb        # Customers related
│   │   ├── ERP_px_cat_g1v2.ipynb     # Products related
│   │
│   └── gold/
│       ├── Gold_preparation.ipynb    # Denormalization
│
├── datesets/
│   ├── crm/          # contains Customers, Products, and Sales details
│   └── erp/          # contains 2 Customers and 1 Products file
│
├── tests/
│   └── Silver_crm_prd_info.ipynb
│   └── Silver_crm_sales_details.ipynb
│   └── Silver_erp_cust_az12.ipynb
│   └── Silver_erp_loc_a101.ipynb
│   └── Silver_erp_px_cat_g1v2.ipynb
│   └── test_Gold.ipynb
|
└── README.md
```


## 🛠️ Tech Stack
 
| Component | Technology | Purpose |
|---|---|---|
| Platform | Databricks | Unified analytics & compute |
| Storage Format | Delta Lake | ACID tables, time travel, schema evolution |
| Processing Engine | Apache Spark (PySpark) | Distributed batch transformations |
| Governance | Unity Catalog | Access control, lineage, discoverability |
| Orchestration | Databricks Workflows | DAG-based job scheduling |
| Language | PySpark + Spark SQL | Transformations and DDL |

## Stay Connected

Let's stay in touch! Feel free to connect with me:

[LinkedIn](https://www.linkedin.com/in/zohaib-sheraz-mughal-08b972163/)   
[zohaibsheraz80attherate(googlemail)dotcom](https://gmail.com/)
