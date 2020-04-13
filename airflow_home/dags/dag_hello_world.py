from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


def print_hello():
    print("Writing to txt")
    with open('.../Airflow/hello_text.txt', 'a+', encoding='utf8') as f:
        f.write(str(datetime.now()) + '\n')
    return 'Hello world!'


dag = DAG('hello_world', description='Returns Hello world',
          schedule_interval='*/1 * * * *',
          start_date=datetime(2020, 4, 13), catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

dummy_operator >> hello_operator
