# IDOR leads to PII Leak

## Report Details
- **Report ID**: 2586584
- **URL**: https://hackerone.com/reports/2586584
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-07-04T16:34:30.054Z
- **Disclosed**: 2024-07-19T15:06:27.105Z

## Reporter
- **Username**: prakhar0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hii Triager,

Through research, I discovered a vulnerability in DoD, that **exposes other users' email addresses through IDOR.**

Vulnerable domain: `www.███████`

## Step To Reproduce

1 - Naviagate to https://www.█████████/ , Create an account.
2 - Go to `Update Profile` Section i..e -> *`https://www.█████/JOINOnline/UpdateProfile/<user-id>`*
3 - Change the *Numeric* `user-id` to any other, and you'll see other user's email-addresses.

## Impact

1 - Leaks Users Email (PII) and Name
2 - IDOR

## System Host(s)
www.███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
## Step To Reproduce

1 - Naviagate to https://www.████████/ , Create an account.
2 - Go to `Update Profile` Section i..e -> *`https://www.███████/JOINOnline/UpdateProfile/<user-id>`*
3 - Change the *Numeric* `user-id` to any other, and you'll see other user's email-addresses.

## Suggested Mitigation/Remediation Actions
1 - Chain the User session with user-id in the backend



## Attachments
No attachments
