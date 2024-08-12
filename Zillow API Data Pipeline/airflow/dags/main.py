from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor 
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
from datetime import timedelta, datetime
import json
import requests


# Load JSON config file (assuming it's valid JSON)
try:
    with open('/home/ubuntu/airflow/config_api.json', 'r') as config_file:
        api_host_key = json.load(config_file)
except FileNotFoundError:
    print("Error: config_api.json not found. Please ensure the file exists.")
    raise

now = datetime.now()
dt_now_string = now.strftime("%d%m%Y%H%M%S")


def extract_zillow_data(**kwargs):
    url = kwargs['url']
    headers = kwargs['headers']
    querystring = kwargs['querystring']
    dt_string = kwargs['date_string']

    # Make the request and handle potential errors
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error extracting data: {e}")
        raise

    # Specify the output file paths
    output_file_path = f"/home/ubuntu/response_data_{dt_string}.json"
    file_str = f'response_data_{dt_string}.csv'

    # Write the JSON response to a file
    with open(output_file_path, "w") as output_file:
        json.dump(response_data, output_file, indent=4)

    output_list = [output_file_path, file_str]
    return output_list


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 10),
    'email': ['aba.issa88@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(seconds=15)
}


with DAG('zillow_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    extract_zillow_data_var = PythonOperator(
        task_id='tsk_extract_zillow_data_var',
        python_callable=extract_zillow_data,
        op_kwargs={
            'url': 'https://zillow56.p.rapidapi.com/search',
            'querystring': {"location": "kansas city, mo"},
            'headers': api_host_key,
            'date_string': dt_now_string
        }
    )
    
    load_to_s3 = BashOperator(
        task_id='tsk_load_to_s3',
        bash_command='aws s3 mv {{ ti.xcom_pull("tsk_extract_zillow_data_var")[0] }} s3://airflow-weather-api-bucket'
    )

    extract_zillow_data_var >> load_to_s3