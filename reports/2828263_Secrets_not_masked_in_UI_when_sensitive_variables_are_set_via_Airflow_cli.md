# Secrets not masked in UI when sensitive variables are set via Airflow cli

## Report Details
- **Report ID**: 2828263
- **URL**: https://hackerone.com/reports/2828263
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-11-07T08:41:45.241Z
- **Disclosed**: 2024-12-30T14:31:29.747Z

## Reporter
- **Username**: saurabhb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
When a sensitive variable is set using Airflow cli, it should be masked on every instance where it is referenced in the UI. However it has been observed that it is masked on the Variable List page and other pages but not the Audit logs page.

Allocated CVE: CVE-2024-50378

Apache Airflow release notes that confirm about fixing the issue in latest release 2.10.3: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html#airflow-2-10-3-2024-11-04

Pull request that fix the issue: https://github.com/apache/airflow/pull/43123

Email communication between me (reporter) and the security team of Apache Airflow:

 {F3741395}

## Impact

Sensitive information disclosed on UI without masking.

## Attachments
No attachments
