# Secrets can be unmasked in the "Rendered Template"

## Report Details
- **Report ID**: 2209665
- **URL**: https://hackerone.com/reports/2209665
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-10-15T09:40:05.284Z
- **Disclosed**: 2023-11-29T19:28:58.172Z

## Reporter
- **Username**: klexadoc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## Affected versions
Apache Airflow before 2.7.1

## How to reproduce

Go to the `Rendered Template` page and in address line replace encoded symbols of `execution_date` parameter with decoded symbols. Page is still shown, but with credentials unmasked.

Sibling pages in contrast have different behavior: `K8s Pod Specs` shows oops page and ` Log` shows empty log when`execution_date` parameter is malformed

## Example
```
not masked - http://airflow.dev.local/rendered-templates?dag_id=tutorial_taskflow_api&task_id=extract&execution_date=2023-08-17T16%3A15%3A08.189107+00%3A00
masked     - http://airflow.dev.local/rendered-templates?dag_id=tutorial_taskflow_api&task_id=extract&execution_date=2023-08-17T16%3A15%3A08.189107%2B00%3A00
```

{F2774937}
{F2774939}

Example dag code:
```python
import json

import pendulum

from airflow.decorators import dag, task
from airflow.models import Variable
@dag(
    schedule=None,
    start_date=pendulum.datetime(2023, 8, 17, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def tutorial_taskflow_api():

    @task()
    def extract(pwd):
        return pwd


    order_data = extract(pwd = Variable.get('secret_var'))
    print(order_data)


tutorial_taskflow_api()
```

In airflow UI variable with name `secret_var` should be added before trying

## Impact

Any user who can see a dag can get access to secret credentials used by this dag

## Attachments
- image.png
- image.png
