import time
from datetime import datetime, timezone
import re

import requests
from requests.auth import HTTPBasicAuth
from requests_html import HTMLSession, HTMLResponse


def dynamic_list():

    name, i = [], 1

    while True:
        cat_name = input(f"Please enter name of {str(i)} cat (or enter nothing to end): ")

        if cat_name == '':
            break

        name.append(cat_name)
        i += 1

    if len(name) == 0:
        print("Seems like you do not own any cats (yet) :(")

    else:
        print(f"We welcome {','.join(name)} to our small cat-house!! :)")


if __name__ == '__main__':
    airflow_api_url = 'https://dev-airflow.deepintent.com/api/v1'
    dag_id = 'segment_size_dag'
    trigger_dag_url = f'{airflow_api_url}/dags/{dag_id}/dagRuns'

    auth = ('admin', 'admin')

    # Record Trigger Time
    trigger_time = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M')
    response = requests.post(trigger_dag_url, auth=auth, json={"conf": {}})

    api_url = f'https://dev-airflow.deepintent.com/api/v1/dags/{str(dag_id)}/dagRuns?start_date_gte={str(trigger_time)}'
    response_2 = requests.get(api_url, auth=HTTPBasicAuth('admin', 'admin'))
    start_time = datetime.now()
    response_json = response_2.json()
    print()
    time.sleep(4)

    while True:
        if str(response_json['total_entries']) != '0':
            end_time = datetime.now()
            print("time taken", end_time - start_time)
            break
        time.sleep(2)
        response_2 = requests.get(api_url, auth=HTTPBasicAuth('admin', 'admin'))
        response_json = response_2.json()
        print(response_json)
