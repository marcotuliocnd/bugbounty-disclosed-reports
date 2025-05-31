# Client side authentication leads to Auth Bypass

## Report Details
- **Report ID**: 1877989
- **URL**: https://hackerone.com/reports/1877989
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-02-17T19:46:50.505Z
- **Disclosed**: 2023-03-24T17:28:11.268Z

## Reporter
- **Username**: kalkii
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi Team

I have found  that to access the data of endpoint ```https://████████/███/?#/``` as user has to submit a password/passphrase.
When we provide wrong password then we get and error message asked to get pass assistance message  ```Contact ████ for password assistance.``` 
After analyzing the JS file I found that when correct password is provide a parameter is set in the localstorage "███████:true"

## Impact

Auth bypass lead to sensitive data exposer like phone number, email id etc.

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Visit https://███/█████/?#/
2. Set a new parameter in local storage name ```█████``` and value ```true```
3. Reload the page

█████

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
