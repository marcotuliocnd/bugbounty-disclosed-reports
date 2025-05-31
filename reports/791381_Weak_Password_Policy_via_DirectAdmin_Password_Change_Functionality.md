# Weak Password Policy via DirectAdmin Password Change Functionality

## Report Details
- **Report ID**: 791381
- **URL**: https://hackerone.com/reports/791381
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-02-08T23:17:06.689Z
- **Disclosed**: 2024-10-22T03:22:15.041Z

## Reporter
- **Username**: seqode
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: endless_group

## Vulnerability Information
## Summary:
*The product does not require that users should have strong passwords, which makes it easier for attackers to compromise user accounts.*

## Steps To Reproduce:
1. Log In at https://da.theendlessweb.com:2222/
2. Go to https://da.theendlessweb.com:2222/user/password?redirect=yes fill your current password and choose a password like a 1234 or 0000

## Potential Mitigations
Enforce usage of strong passwords. A password strength policy should contain the following attributes:
1. Minimum and maximum length;
2. Require mixed character sets (alpha, numeric, special, mixed case);
3. Do not contain user name;
4. Expiration;
5. No password reuse.

## References:
https://cwe.mitre.org/data/definitions/521.html

## Impact

An authentication mechanism is only as strong as its credentials. For this reason, it is important to require users to have strong passwords. Lack of password complexity significantly reduces the search space when trying to guess user's passwords, making brute-force attacks easier.

## Attachments
- 1._POC.png
- 2._POC_Confirmation.png
