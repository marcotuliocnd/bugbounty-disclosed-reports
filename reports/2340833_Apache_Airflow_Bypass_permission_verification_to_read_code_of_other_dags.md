# Apache Airflow: Bypass permission verification to read code of other dags

## Report Details
- **Report ID**: 2340833
- **URL**: https://hackerone.com/reports/2340833
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-01-31T07:20:56.083Z
- **Disclosed**: 2024-03-12T02:19:57.277Z

## Reporter
- **Username**: timon8
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Apache Airflow, versions before 2.8.1, have a vulnerability that allows an authenticated user to access the source code of a DAG to which they don't have access. This vulnerability is considered low since it requires an authenticated user to exploit it. Users are recommended to upgrade to version 2.8.1, which fixes this issue.

**Email form the project maintainer**
██████████

## Impact

Apache Airflow<2.8.1

## Attachments
No attachments
