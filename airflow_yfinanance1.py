
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import boto3
import logging
from botocore.exceptions import ClientError
import logging
from botocore.exceptions import ClientError
import os
import zipfile
from zipfile import ZipFile
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
import pymysql

default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': days_ago(2),
        'email': ['preetisehgal2001@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),

    }

dag = DAG(
        dag_id='yfinanace1_dag',
        default_args=default_args,
        description='Tesla stock data from yfinanace API',
        schedule_interval=timedelta(days=1),
    )

t1 = BashOperator(
        task_id='run_yfinannce_api',
        bash_command='kaggle datasets download -d jordangoblet/atp-tour-20002016 -p /Users/psehgal/atp_test',
        dag=dag,
    )
t2 = PythonOperator(
    task_id='unzip_api',
    provide_context=False,
    python_callable=unzip,
    dag=dag,
)

t3 = PythonOperator(
        task_id='move_file_to_AWS_S3',
        provide_context=False,
        python_callable=insert_data,
        dag=dag
)

t4 = PythonOperator(
        task_id='move_data_from_file_to_SQL',
        provide_context=False,
        python_callable=insert_sql,
        dag=dag,
)

t5 = PythonOperator(
        task_id='remove_file',
        provide_context=False,
        python_callable=remove_files,
        dag=dag,
)