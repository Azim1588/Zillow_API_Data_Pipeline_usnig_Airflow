# Zillow_API_Data_Pipeline_usnig_Airflow

This project is a data pipeline that extracts real estate data from the Zillow API, processes it, and then stores it in an AWS S3 bucket. The entire process is orchestrated using Apache Airflow.

## Table of Contents

- [Introduction](#introduction)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Airflow DAG Details](#airflow-dag-details)


## Introduction

This pipeline automates the process of extracting real estate data from Zillow, transforming it into a desired format (JSON to CSV), and then uploading it to an S3 bucket for storage or further processing. The pipeline is managed using Apache Airflow, allowing for scheduling, monitoring, and maintaining data workflows.

## Architecture

The data pipeline consists of the following steps:

1. **Extraction**: Data is extracted from the Zillow API based on predefined query parameters.
2. **Transformation**: The extracted JSON data is converted into CSV format.
3. **Load**: The transformed CSV data is uploaded to an AWS S3 bucket.
4. **Orchestration**: Apache Airflow orchestrates the entire process.

![Pipeline Architecture](./assets/architecture_diagram.png)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Apache Airflow**: Installed and configured on your system.
- **AWS CLI**: Configured with appropriate credentials for accessing S3.
- **Python 3.x**: With necessary libraries such as `requests` and `boto3` installed.
- **Zillow API Key**: Access key for Zillow's API.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Azim1588/zillow-data-pipeline.git
   cd zillow-data-pipeline

## Set up Airflow:

- Ensure that Airflow is correctly installed and configured.
- Place the DAG file (`zillow_dag.py`) in your Airflow `dags/` directory.

## Configuration

### Zillow API Configuration:

Create a configuration file (`config_api.json`) to store your Zillow API credentials and other necessary headers.

```json
{
  "x-rapidapi-host": "zillow56.p.rapidapi.com",
  "x-rapidapi-key": "YOUR_API_KEY"
}
```

### S3 Bucket Configuration:

Set up an S3 bucket where the CSV files will be stored. Update the DAG to point to the correct bucket.

## Usage

### Start Airflow:

- Ensure that the Airflow web server and scheduler are running.

### Trigger the DAG:

- You can manually trigger the DAG from the Airflow UI or set it to run on the defined schedule (`@daily` by default).

### Monitor the Pipeline:

- Use the Airflow UI to monitor the execution of the DAG, check logs, and view the status of each task.

## Airflow DAG Details

### Tasks

- **Extract Zillow Data**:
  - **Task ID**: `tsk_extract_zillow_data_var`
  - **Description**: Fetches real estate data from the Zillow API and saves it as a JSON file.

- **Transform JSON to CSV**:
  - **Task ID**: `tsk_json_to_csv_var`
  - **Description**: Converts the extracted JSON data into CSV format.

- **Upload to S3**:
  - **Task ID**: `tsk_load_to_s3`
  - **Description**: Uploads the transformed CSV file to the specified S3 bucket.

### DAG Configuration

```python
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 10),
    'email': ['your.email@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(seconds=15)
}

with DAG('zillow_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:
    ...

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 10),
    'email': ['your.email@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(seconds=15)
}

with DAG('zillow_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:
    ...
