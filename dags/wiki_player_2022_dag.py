from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from datetime import timedelta
from etl.wiki_wc_player_2022_etl import extract_player_data, transform_wrapper, load_wrapper
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
    dag_id='fifa_player_data_flow',
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


extract_player_data = PythonOperator(
    task_id="extract_player_data",
    python_callable=extract_player_data,
    provide_context=True,
    op_kwargs={"url": "https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_squads"},
    dag=dag
)


transform_player_data = PythonOperator(
    task_id='transform_player_data',
    python_callable=transform_wrapper,
    provide_context=True,
    dag=dag
)


load_player_data = PythonOperator(
    task_id='load_player_data',
    python_callable=load_wrapper,
    provide_context=True,
    op_kwargs={"file_name": "FIFA_World_Cup_2022_players.csv"},
    dag=dag
)

end = PythonOperator(
    task_id="end",
    python_callable = lambda: print("Jobs completed successfully"),
    dag=dag
)

# Set up task dependencies
start >> extract_player_data >> transform_player_data >> load_player_data >> end