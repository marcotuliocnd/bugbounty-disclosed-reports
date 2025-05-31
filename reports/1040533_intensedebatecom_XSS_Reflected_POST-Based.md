# [intensedebate.com] XSS Reflected POST-Based 

## Report Details
- **Report ID**: 1040533
- **URL**: https://hackerone.com/reports/1040533
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-11-22T12:04:54.232Z
- **Disclosed**: 2021-01-15T21:20:46.577Z

## Reporter
- **Username**: fuzzme
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hello, i have found a XSS Reflected POST-Based in `https://www.intensedebate.com/ajax.php`.

Vulnerable(s) URL :

```POST /https://www.intensedebate.com/ajax.php```

Vulnerable(s) Parameter(s):

```
$_POST['txt'];
```

Payload

```
azertyuiop<<><img+src="x"/onerror="prompt(document.cookie)">
```

##Steps to reproduce
1. Open the xss.html and will you see a javascript pop-up

You can  also follow me into the video POC.

Thank you, good bye.

## Impact

A attacker can perform a phishing attack or perform a CORS attack

## Attachments
- xss.html
- xss.mp4
