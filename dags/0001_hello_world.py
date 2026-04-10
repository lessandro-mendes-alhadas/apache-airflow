"""
Primeira DAG do Airflow neste projeto!
"""
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# 1. Definição dos argumentos padrão
default_args = {
    'owner': 'Lessandro Alhadas',
    'depends_on_past': False,
    'start_date': datetime(2026, 4, 10),
    'retries': 0
}

# 2. Definição da DAG
with DAG(
    '0001_hello_world',
    default_args=default_args,
    description='DAG Hello World',
    doc_md=__doc__,
    catchup=False
) as dag:

    # 3. Definição da Tarefa
    task = BashOperator(
        task_id='hello_world_task',
        bash_command='echo "Hello World!"',
    )

# 4. Definindo a ordem de execução (aqui, apenas uma tarefa)
task