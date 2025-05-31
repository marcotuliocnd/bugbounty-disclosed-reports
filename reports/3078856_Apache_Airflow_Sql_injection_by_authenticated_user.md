# Apache Airflow Sql injection by authenticated user

## Report Details
- **Report ID**: 3078856
- **URL**: https://hackerone.com/reports/3078856
- **State**: Closed
- **Severity**: low
- **Submitted**: 2025-04-05T06:10:57.402Z
- **Disclosed**: 2025-05-27T17:55:18.470Z

## Reporter
- **Username**: nxczje
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Apache Airflow, versions 2.10.5, is affected by a vulnerability that allows an attacker can manipulate query construction, leading to an SQL Injection vulnerability that may result in remote code execution.

## Impact

The DAGS that use the SQLColumnCheckOperator in the system will remote code execution.

## Attachments
No attachments
