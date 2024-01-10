from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from datetime import timedelta
from etl.wiki_wc_match_etl import extract_match_data, transform_match_data, load_match_data
from etl.aws_wc_match_etl import *
import os
import sys 
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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
    dag_id='world_cup_match_data_flow',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
)

# Define PythonOperator tasks

start = PythonOperator(
    task_id="start",
    python_callable = lambda: print("Jobs started"),
    dag=dag
)

extract_match_data = PythonOperator(
    task_id="extract_match_data",
    python_callable=extract_match_data,
    provide_context=True,
    op_kwargs={"year": "{{ execution_date.year }}"},  # Use Airflow execution_date to get the year dynamically
    dag=dag
)

transform_match_data = PythonOperator(
    task_id='transform_match_data',
    python_callable=transform_match_data,
    provide_context=True,
    op_kwargs={"years": [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]},
    dag=dag
)

load_match_data = PythonOperator(
    task_id='load_match_data',
    python_callable=load_match_data,
    provide_context=True,
    op_kwargs={"file_name": "data/world_cup_match.csv"},
    dag=dag
)


end = PythonOperator(
    task_id="end",
    python_callable = lambda: print("Jobs completed successfully"),
    dag=dag
)

# Set up task dependencies
start >> extract_match_data >> transform_match_data >> load_match_data >> end