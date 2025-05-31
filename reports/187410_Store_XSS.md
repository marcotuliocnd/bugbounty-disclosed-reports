# Store XSS

## Report Details
- **Report ID**: 187410
- **URL**: https://hackerone.com/reports/187410
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-12-01T17:55:00.658Z
- **Disclosed**: 2017-01-01T20:46:32.675Z

## Reporter
- **Username**: imran_hadid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Hello Team.

I found a Store XSS. Where the company name is the vulnerable to XSS. If you give this below XSS script as Company name, you will get the XSS pop up after the login in message option where it'll randomly generated at the message room.
“><IMG SRC=x onerror=javascript:alert(&quot;XSS-by-Imran&quot;)> 

 Here is the POC:
https://youtu.be/dqrH2WhIgtk

Thanks


## Attachments
No attachments
