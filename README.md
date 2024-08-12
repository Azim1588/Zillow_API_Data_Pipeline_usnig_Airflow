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
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

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

