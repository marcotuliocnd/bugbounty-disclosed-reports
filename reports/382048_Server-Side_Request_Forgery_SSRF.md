# Server-Side Request Forgery (SSRF)

## Report Details
- **Report ID**: 382048
- **URL**: https://hackerone.com/reports/382048
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-16T13:13:13.567Z
- **Disclosed**: 2019-12-02T19:09:40.073Z

## Reporter
- **Username**: t-pwn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi,

I've found a Server-Side Request Forgery (SSRF)

Steps to reproduce:

+ start listening on your server 
+ navigate to http://██████/help/ACPS.htm#http://$yourserver:$port
+ you will get the request

██████

## Impact

Server-Side Request Forgery (SSRF) Attack

## Attachments
No attachments
