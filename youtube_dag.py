from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from youtube_etl import run_youtube_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email': ['airflow@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    'youtube_dags',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval=timedelta(days=1),
) as dag:

    run_etl = PythonOperator(
        task_id='complete_youtube_etl',
        python_callable=run_youtube_etl,
    )

    # Dummy task to run after the ETL task
    dummy_task = DummyOperator(
        task_id='dummy_task',
    )

    # Set the task dependencies
    run_etl >> dummy_task

# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'start_date': datetime(2020, 11, 8),
#     'email': ['airflow@gmail.com'],
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=1)
# }

# dag = DAG(
#     'youtube_dags',
#     default_args=default_args,
#     description='Our first DAG with ETL process!',
#     schedule_interval=timedelta(days=1),
# )

# run_etl = PythonOperator(
#     task_id='complete_youtube_etl',
#     python_callable=run_youtube_etl,
#     dag=dag, 
# )

# # Dummy task to run after the ETL task
# # dummy_task = DummyOperator(
# #     task_id='dummy_task',
# #     dag=dag,
# # )

# # Set the task dependencies
# run_etl 
# # >> dummy_task