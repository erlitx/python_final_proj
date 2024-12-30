from datetime import datetime

from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.operators.python import PythonOperator

from usecase.data_marts import sale_analisys


with DAG(
    dag_id="data_marts",
    start_date=datetime(2023, 12, 1),
    catchup=False,
    tags=["data_marts"],
) as dag:
        
        data_mart_sales = PythonOperator(
        task_id="sale_analisys",
        python_callable=sale_analisys,
        )

data_mart_sales 
