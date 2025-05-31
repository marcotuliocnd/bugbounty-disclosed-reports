# Improper Authentication (Login without Registration with any user) at ████

## Report Details
- **Report ID**: 2334420
- **URL**: https://hackerone.com/reports/2334420
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-01-25T13:29:10.107Z
- **Disclosed**: 2024-03-22T17:50:41.409Z

## Reporter
- **Username**: archyxsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi Team!

I found a security issue in ███████. An attacker could login as a any user without registration in the page and above all it can change the session of a victim and authenticate him as any user. 

The problem is at the endpoint  ██████████ which, thanks to the **signin** parameter, allows to authenticate anyone with any user.

## Impact

Authentication bypass (Login as any user without authentication)
Force a victim to change session with other user

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go to ██████████
2. To check the authentication bypass go to ████:

███

As the link corresponds to a GET request you can force any user to log out and authenticate to any other account.

Additional bonus: *clientid and clientsecret are stored in the page source*

███████

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
