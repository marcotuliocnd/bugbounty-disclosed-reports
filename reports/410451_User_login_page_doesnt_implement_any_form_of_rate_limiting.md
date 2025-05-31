# User login page doesn't implement any form of rate limiting

## Report Details
- **Report ID**: 410451
- **URL**: https://hackerone.com/reports/410451
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-17T05:54:18.802Z
- **Disclosed**: 2019-01-04T11:00:10.295Z

## Reporter
- **Username**: 0xspade
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi Team,

**Summary:**
As a best practice a login page should have a rate limitting just like hackerone.com

**Vulnerable Request**
```
POST /auth/post_login HTTP/1.1
Host: ctf.hacker101.com
User-Agent: <redacted>
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://ctf.hacker101.com/
Content-Type: application/x-www-form-urlencoded
Content-Length: 73
Cookie:<some cookie>
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1

csrf=<csrf token>&username=<target username>&password=<vulnerable parameter>
```
### Steps To Reproduce

1. Tamper login page and send the request to Burp Intruder
2. Configure the payloads
3. Start the Burp Intruder

**Proof Of Concept**
██████

Notice the Content Length as highlited on my screenshot

## Impact

An attacker can freely bruteforce any username and can takeover any account

## Attachments
No attachments
