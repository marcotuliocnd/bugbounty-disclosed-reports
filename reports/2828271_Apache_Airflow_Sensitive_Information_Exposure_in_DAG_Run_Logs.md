# Apache Airflow: Sensitive Information Exposure in DAG Run Logs

## Report Details
- **Report ID**: 2828271
- **URL**: https://hackerone.com/reports/2828271
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-11-07T08:50:20.562Z
- **Disclosed**: 2024-12-30T14:40:35.177Z

## Reporter
- **Username**: saurabhb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The passwords, secrets and fernet key are logged in plain text in logs. This is insecure because they should be masked in logs. Logs can be accessed by unauthorized users and this can result in disclosing of this sensitive information to them.

Allocated CVE: CVE-2024-45784

Apache Airflow release notes that confirm about fixing the issue in latest release 2.10.3: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html#airflow-2-10-3-2024-11-04

Pull request that fix the issue: https://github.com/apache/airflow/pull/43040

Email communication between me (reporter) and the security team of Apache Airflow:

{F3741452}

## Impact

Disclosure of secrets to unauthorized users via logs.

## Attachments
No attachments
