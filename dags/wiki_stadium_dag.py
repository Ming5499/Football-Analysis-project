from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from datetime import timedelta
import os
import sys 
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from etl.wiki_stadium_etl import extract_wikipedia_stadium_data, transform_wikipedia_data, load_to_csv_wikipedia_data
    
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
    dag_id='wiki_stadium_flow',
    default_args=default_args,
    schedule_interval = None,
    catchup=False    
)

# Define PythonOperator tasks

start = PythonOperator(
    task_id="start",
    python_callable = lambda: print("Jobs started"),
    dag=dag
)

extract_data_from_wikipedia = PythonOperator(
    task_id="extract_data_stadium_from_wikipedia",
    python_callable=extract_wikipedia_stadium_data,
    provide_context=True,
    op_kwargs={"url": "https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity"},
    dag=dag
)

transform_wikipedia_data = PythonOperator(
    task_id='transform_wikipedia_data',
    provide_context=True,
    python_callable=transform_wikipedia_data,
    dag=dag
)

load_wikipedia_data = PythonOperator(
    task_id='load_wikipedia_data',
    provide_context=True,
    python_callable=load_to_csv_wikipedia_data,
    dag=dag
)


end = PythonOperator(
    task_id="end",
    python_callable = lambda: print("Jobs completed successfully"),
    dag=dag
)

# Set up task dependencies
start >> extract_data_from_wikipedia >> transform_wikipedia_data >> load_wikipedia_data >> end