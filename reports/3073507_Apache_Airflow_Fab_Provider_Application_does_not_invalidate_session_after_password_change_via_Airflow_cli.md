# Apache Airflow Fab Provider: Application does not invalidate session after password change via Airflow cli

## Report Details
- **Report ID**: 3073507
- **URL**: https://hackerone.com/reports/3073507
- **State**: Closed
- **Severity**: low
- **Submitted**: 2025-04-02T10:40:17.010Z
- **Disclosed**: 2025-05-29T12:43:25.455Z

## Reporter
- **Username**: saurabhb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
When a user changes his password by visiting `/resetmypassword` form, the application terminates all the existing sessions. This is to defend against the attack scenario when a user believes his account is hacked and so changes the password to ensure that he/she is the only one knowing the password in case the old password was compromised or session-id was compromised let us say using an XSS attack and then the application logs out all users making sure the attacker is also logged out and the legitimate user can safely log back in using the new password. However it has been observed that the application fails to terminate existing sessions if the password change was done by airflow cli tool.

Allocated CVE: [CVE-2024-45033](https://lists.apache.org/thread/yw535346rk766ybzpqtvrl36sjj789st)

Advisory: https://github.com/advisories/GHSA-8863-4qmg-fr45

Pull request that fix the issue: https://github.com/apache/airflow/pull/45139

Email communication between me (reporter) and the security team of Apache Airflow:
{F4208960}

## Impact

Account takeover possibility due to insufficient session expiration vulnerability in Apache Airflow Fab Provider.

## Attachments
- image.png
