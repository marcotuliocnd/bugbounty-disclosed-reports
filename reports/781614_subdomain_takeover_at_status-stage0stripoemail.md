# subdomain takeover at status-stage0.stripo.email

## Report Details
- **Report ID**: 781614
- **URL**: https://hackerone.com/reports/781614
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-23T15:40:37.720Z
- **Disclosed**: 2020-01-30T10:14:21.187Z

## Reporter
- **Username**: laz0rde
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
The subdomain status-stage0.stripo.email was pointed at uptimerobot.com
whereas it was not being used , but having Cname record as stats.uptimerobot.com .
Hence anyone can takeover it.

I have parked it with an account on uptimerobot.com
note : 
this issue is similar to [report](https://hackerone.com/reports/737695)
but with another subdomain

## Impact

Subdomain takeover can be abused to do several things like :

Malware distribution
Phishing / Spear phishing
XSS
Authentication bypass
Legitimate mail sending and receiving on behalf of ford subdomain
...
List goes on and on

## Attachments
- 100.png
- poc.png
