# 🍕 FSB Pizza Data Pipeline (End-to-End ETL)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Google BigQuery](https://img.shields.io/badge/Google_Cloud-BigQuery-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📋 Project Overview
**FSB Pizza Data Pipeline** is a robust Data Engineering project designed to consolidate sales and operational data from a pizza restaurant chain.

This project simulates a real-world scenario where data is ingested from REST APIs, cleaned and transformed using **Python (Pandas)**, and loaded into a **Google BigQuery** Data Warehouse. The pipeline is built with a **modular architecture** to ensure scalability, maintainability, and ease of testing.

**Key Features:**
* **Modular ETL Design:** Separation of concerns (Extract, Transform, Load) for better code management.
* **Incremental Loading:** Logic to handle daily data ingestion via date parameters.
* **Cloud-Native:** Fully integrated with Google Cloud Platform (BigQuery).
* **Secure:** Uses Service Account authentication (not hardcoded credentials).

## 🏗️ Architecture & Project Structure

The project follows a production-ready directory structure:

fsb-data-pipeline/
│
├── config/              # Configuration files (YAML)
│   └── config.yaml      # Database & API configurations
│
├── etl/                 # Core ETL Logic Modules
│   ├── extract.py       # Fetches raw data from API
│   ├── transform.py     # Cleans & formats data (Type casting, etc.)
│   └── load.py          # Uploads data to BigQuery
│
├── pipelines/           # Orchestration Scripts
│   └── ingest_data.py   # Main entry point to run the pipeline
│
├── src/                 # Shared Utilities
│   └── schema_generator.py    # Helper functions (BigQuery Connection)
│   └── connect_gbq.py         # Helper functions (Schema Gen)
│
├── notebooks/           # Jupyter Notebooks for experimentation
│   └── google-colab.ipynb
│
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

## 🚀 Prerequisites
* Before running the pipeline, ensure you have:
* Python 3.8+ installed.
* Google Cloud Platform (GCP) account with BigQuery enabled.
* Service Account Key (JSON) with BigQuery Admin or Data Editor role.

## 🛠️ Installation & Setup
* Clone the Repository

Bash
git clone [https://github.com/username-mas-fajar/fsb-data-pipeline.git](https://github.com/username-mas-fajar/fsb-data-pipeline.git)
cd fsb-data-pipeline

* Install Dependencies
It is recommended to use a virtual environment.

Bash
pip install -r requirements.txt
Configure Credentials

* Place your GCP Service Account JSON key in the config/ folder.

IMPORTANT: Rename the file or update config/config.yaml to match your key filename.
Note: The JSON key is git-ignored for security.

* Update Configuration
Edit config/config.yaml to match your Project ID:

YAML
project_id: "de-fsb-2026"
api_base_url: "[https://fsbproject.vercel.app/](https://fsbproject.vercel.app/)"
service_account_key: "config/your-key-file.json"

## ▶️ Usage
To run the pipeline for a specific dataset (e.g., Orders), run the following command from the root directory:

Bash
python -m pipelines.ingest_data \
  --data_name="order" \
  --dataset_name="data_landing" \
  --dest_table_name="trx_orders"

Arguments:
--data_name: Endpoint name from the API (e.g., order, customer, pizza).
--dataset_name: Destination Dataset ID in BigQuery.
--dest_table_name: Destination Table ID in BigQuery.

## 📊 Dashboard
![Dashboard Preview](docs/dashboard_v1.png)

https://lookerstudio.google.com/reporting/f9424be0-a07f-4aef-b90a-16bf235ab472
The final data is visualized in Looker Studio to track Sales Performance and Customer Trends.

## 👤 Author
Fajar Aji Pamungkas
LinkedIn: linkedin.com/in/fajaraji25
GitHub: github.com/fajaraji

Created as part of the FullStack Bangalore Data Engineering Bootcamp Final Project.