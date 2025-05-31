# Reflected xss in https://sh.reddit.com

## Report Details
- **Report ID**: 1549206
- **URL**: https://hackerone.com/reports/1549206
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-04-24T06:11:22.525Z
- **Disclosed**: 2022-05-08T07:36:43.558Z

## Reporter
- **Username**: abhiramsita
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
Reflected cross-site scripting (or XSS) arises when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way.

## Impact:
attacker can execute malicious java script and steal cookies 

## Steps To Reproduce:
[add details for how we can reproduce the issue]

Hi team ,

Navigate to below url 
scroll to page end find a option see more
Move mouse over there and observe the execution of javascript 
## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

attacker can execute malicious java script and steal cookies

## Attachments
No attachments
