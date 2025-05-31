# Stored XSS at https://█████

## Report Details
- **Report ID**: 1620247
- **URL**: https://hackerone.com/reports/1620247
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-06-30T11:47:10.088Z
- **Disclosed**: 2022-09-06T19:04:09.997Z

## Reporter
- **Username**: nomore_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
In registeration page ( https://████ ) , first name and last name field are vulnerable to Stored Cross Site Scripting.

## Proof of concept
For the fastly test, use this credentials to login (my test account)
> email: █████████
password: ██████

After login , alert document.cookie will triggered

## Impact

Stored Cross Site Scripting which attacker can execute malicious javascript payload.

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go to registration page ( https://████ ), insert `<svg/onload=confirm(document.cookie)>` payload in firstname and lastname fields and create account.
2. Verified your account.
3. Go to login page and login your account.
4. And XSS will triggered ( XSS also triggered in `My Profile` page) .

## Suggested Mitigation/Remediation Actions
1. Filter input on arrival.
2. Encode data on output.
3. Content Security Policy



## Attachments
No attachments
