"""
Minha primeira DAG no Airflow
"""
from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

# 1. Definição dos argumentos padrão
default_args = {
    'owner': 'Lessandro Alhadas',
    'depends_on_past': False,
    'start_date': datetime(2026, 9, 6),
    'retries': 0
}

# 2. Definição da DAG
with DAG(
    'my_first_dag',
    default_args=default_args,
    description='My First DAG',
    doc_md=__doc__,
    catchup=False
) as dag:

    # 3. Definição da Tarefa
    task1 = BashOperator(
        task_id='task_1',
        bash_command='echo "I\'m the task 1"',
    )

    with TaskGroup(
        group_id='task_group_1',
        tooltip='This is task group 1'
    ) as task_group_1:
        subtask1 = BashOperator(task_id='subtask_1', bash_command='echo "I\'m subtask 1 of task group 1"')
        subtask2 = BashOperator(task_id='subtask_2', bash_command='echo "I\'m subtask 2"')

    task2 = BashOperator(
        task_id='task_2',
        bash_command='echo "I\'m the task 2"',
    )

    task1 >> task_group_1 >> task2