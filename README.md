# Start to work with Airflow
## Creating a simple DAG
Here we create a very simple DAG called *hello_world* and run it through Airflow.
This DAG will write the time in a text file on specified intervals.
### DAG:
Directed Acyclic Graph is a finite directed graph with no directed cycles. This means it is a graph with arrows as
links, and with no loop inside it.
In Airflow DAGs are used to specify workflows. Operators are stored in DAGs, operators define individual tasks.
Common operators are *BashOperator* and *PythonOperator*.

To create and run a simple DAG:
1. Inside your project folder (**Airflow**) create a folder **airflow_home**
2. ```.../Airflow$ export AIRFLOW_HOME='airflow_home' airflow_home ```
3. ```.../Airflow$ airflow version ``` <br />
In *airflow_home* folder, files *airflow.cfg* and *unittest.cfg* will be created.
4. ```.../Airflow$ airflow initdb ``` <br />
Creates *airflow.db* in *airflow_home* folder. It is a SQLLite file that stores configuration data of running workflows.
5. ```.../Airflow$ airflow webserver ``` <br />
Starts the UI on the browser on http://0.0.0.0:8080 .
6. Create  folder **dags** in *airflow_home*. Add your Python DAG file (*dag_hello_world.py*) inside it.
7. In a new terminal:  <br />
```.../Airflow$ export AIRFLOW_HOME='airflow_home' airflow_home ``` <br />
```.../Airflow$ airflow scheduler ``` <br />
Refresh the UI. New DAG with name *hello_world* appears.
8. Turn on the *hello_world* DAG. Check tree view and the text file. <br />
Codes until this stage are [here](dd529c4ad3c872f3885bd539f948f41f5be5d01e
)
