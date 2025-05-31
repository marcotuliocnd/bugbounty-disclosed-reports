# Error Page Content Spoofing or Text Injection 

## Report Details
- **Report ID**: 498562
- **URL**: https://hackerone.com/reports/498562
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-02-20T12:37:22.299Z
- **Disclosed**: 2020-06-03T04:19:40.831Z

## Reporter
- **Username**: ajayshrimali
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: smule

## Vulnerability Information
Description:
--------------


Content spoofing, also referred to as content injection, "arbitrary text injection" or virtual defacement, is an attack targeting a user made possible by an injection vulnerability in a web application. When an application does not properly handle user-supplied data, an attacker can supply content to a web application, typically via a parameter value, that is reflected back to the user. This presents the user with a modified page under the context of the trusted domain.

Steps to Reproduce:
---------------------
  1. Login with valid credentials.
  2. On the application Dashboard, I have searched the malicious query and it will result in the error or data not found. I have leveraged this issue to content spoofing or Text injection attack.


For the Reference
---------------------
1) https://hackerone.com/reports/327671
2) https://hackerone.com/reports/106350

## Impact

This attack is typically used as, or in conjunction with, social engineering because the attack is exploiting a code-based vulnerability and a user's trust. As a side note, this attack is widely misunderstood as a kind of bug that brings no impact.

## Attachments
- POC.png
