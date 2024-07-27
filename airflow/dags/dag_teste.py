from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_oi():
    print("Oi")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
    'test_dag',
    default_args=default_args,
    description='Uma DAG simples para imprimir Oi',
    schedule_interval='@daily',
    catchup=False,
) as dag:
    
    task1 = PythonOperator(
        task_id='print_oi',
        python_callable=print_oi,
    )

task1
