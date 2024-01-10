from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from datetime import timedelta
from etl.aws_wc_match_etl import upload_to_s3
from utils.constants import *
    
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 22),
    'email': ['npam5499@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=3)
}

dag = DAG(
    dag_id='upload_to_s3',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
)

load_to_s3 = PythonOperator(
        task_id='load_to_s3',
        python_callable=upload_to_s3,
        op_kwargs={'folder_path': '/home/ubuntu/data', 'bucket_name': {AWS_BUCKET_NAME}},
    )

load_to_s3