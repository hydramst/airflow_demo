from airflow import DAG
from datetime import datetime, timedelta

default_args = {
    'owner': 'you',
    'start_date': datetime(2022, 1, 1),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('my_dag_1', default_args=default_args, schedule_interval=timedelta(hours=1))

from airflow.operators.python_operator import PythonOperator
import random
import string

def create_files():
    for i in range(100):
        with open(f"file_{i}.txt", "w") as file:
            file.write(''.join(random.choices(string.ascii_letters, k=100)))

create_files_task = PythonOperator(
    task_id='create_files',
    python_callable=create_files,
    dag=dag
)


def count_occurrences():
    for i in range(100):
        with open(f"file_{i}.txt", "r") as file:
            text = file.read()
            count = text.count('a')
            with open(f"file_{i}.res", "w") as res_file:
                res_file.write(str(count))

count_occurrences_task = PythonOperator(
    task_id='count_occurrences',
    python_callable=count_occurrences,
    dag=dag
)


def sum_results():
    total = 0
    for i in range(100):
        with open(f"file_{i}.res", "r") as res_file:
            total += int(res_file.read())
    with open("final_result.txt", "w") as final_file:
        final_file.write(str(total))

sum_results_task = PythonOperator(
    task_id='sum_results',
    python_callable=sum_results,
    dag=dag
)


create_files_task >> count_occurrences_task >> sum_results_task
