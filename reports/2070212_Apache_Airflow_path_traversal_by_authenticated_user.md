# Apache Airflow path traversal by authenticated user

## Report Details
- **Report ID**: 2070212
- **URL**: https://hackerone.com/reports/2070212
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-07-15T03:20:46.347Z
- **Disclosed**: 2023-09-14T17:50:47.985Z

## Reporter
- **Username**: kietna20
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Apache Airflow, versions before 2.6.3, is affected by a vulnerability that allows an attacker to perform unauthorized file access outside the intended directory structure by manipulating the run_id parameter.

## Impact

Denial of Service (DoS): By traversing to system directories and attempting to access large or resource-intensive files, an attacker can cause a denial of service condition. This can lead to system crashes, resource exhaustion, or degraded performance.

## Attachments
No attachments
