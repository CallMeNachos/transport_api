from airflow.operators.python_operator import PythonOperator
from airflow import DAG
from airflow.decorators import task


with DAG(
	dag_id="ovapi_extract",
	schedule_interval='0 0 * * *'
	) as dag:

	@task(task_id="start_task")
	def start_task():
		return "start DAG"

	# @task(task_id="extract_api_task")
	# def extract_api_task():
	# 	from extract import Extract
	# 	# Extract data from API
	# 	url = "https://v0.ovapi.nl/"
	# 	extract = Extract(url)
	# 	df = extract.create_dataframe()
	# 	return df

	@task(task_id="end_task")
	def end_task():
		return "end DAG"

