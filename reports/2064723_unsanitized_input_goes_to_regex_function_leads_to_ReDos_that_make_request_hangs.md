# unsanitized input goes to regex function leads to ReDos that make request hangs

## Report Details
- **Report ID**: 2064723
- **URL**: https://hackerone.com/reports/2064723
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-07-12T08:54:12.530Z
- **Disclosed**: 2023-08-28T16:28:56.866Z

## Reporter
- **Username**: shin24
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Apache Airflow, versions before 2.6.3, has a vulnerability where an authenticated user can use crafted input to make the current request hang

## Impact

this will help attacker achieve Dos attack with less effort

## Attachments
No attachments
