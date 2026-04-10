# apache-airflow
Repository for exercises Apache Airflow

### Instalar a versão correta do Python se ainda não existe
pyenv install 3.11.13

### Definir a versão local
pyenv local 3.11.13

### Cria o Ambiente Virtual
python -m venv venv

### Ativa o Ambiente Virtual
source venv/bin/activate

### Instala as dependências
pip install -r requirements.txt

### Congelar as versões das dependências
pip freeze > requirements-freezed.txt

### Definir a variável de ambiente do Airflow Home
export AIRFLOW_HOME=$(pwd)/airflow_home

### Desabilitar DAGs de exemplo do Airflow com problema
Na pasta \venv\lib\python3.11\site-packages\airflow\example_dags\
Criar o arquivo .airflowignore e adicionar as DAGs

### Inicializa o banco de dados do Airflow
airflow db init

### Configurar a pasta de DAGs do Airflow
No arquivo airflow_home/airflow.cfg atualizar a propriedade dags_folder
dags_folder = /home/lessandro/Workspaces/Python/apache-airflow/dags

### Cria um usuário adminstrador
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email lessandro.alhadas@gmail.com

### Inicia os serviços do Airflow
airflow standalone