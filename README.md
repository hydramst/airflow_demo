# airflow_demo
simple airflow pipeline with 3 tasks

![image](https://user-images.githubusercontent.com/44744458/213933222-45bc80a0-93f2-40dd-9f51-fe99aac854f9.png)


Create a new DAG (Directed Acyclic Graph) in Airflow

Tasks in the flow:
1. Create a task in the DAG to create 100 text files with random characters using the PythonOperator

2. Create a task to count the number of occurrences of the letter 'a' in each file 

3. Create a final task to sum the data in all the .res files using



Here you can find action plan to setup Airflow:

## setup airflow 

To set up Airflow on your Ubuntu virtual environment, you can use the following steps:

1.  Activate your virtual environment: `source myvenv/bin/activate`
2.  Install Airflow: `pip install apache-airflow`
3.  Initialize the Airflow database: `airflow db init`
4.  Start the Airflow webserver: `airflow webserver -p 8080` (or any other port you prefer)
5.  Start the Airflow scheduler: `airflow scheduler`
6.  Verify that the webserver and scheduler are running by accessing the Airflow UI at [http://localhost:8080](http://localhost:8080/) in your web browser.
7.  To stop the webserver and scheduler, use the command `CTRL + C`
8.  To deactivate the virtual environment, use the command `deactivate`.

## create user 

To create a user, you can use the command `airflow create_user` and provide a username, email, and password.

For example:

`airflow users create -r Admin -u admin -e admin@example.com -f admin -l admin -p adminpassword`

This command creates an Admin user with the username "admin", email "[admin@example.com](mailto:admin@example.com)", first name "admin", last name "admin", and password "adminpassword".


## create and run DAG

1. In the ~/airflow/dags directory add python file from this repo

2. Visit http://localhost:8080/home and check how the DAG is working
