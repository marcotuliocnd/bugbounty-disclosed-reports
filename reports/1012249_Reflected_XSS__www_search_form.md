# Reflected XSS  www.█████ search form

## Report Details
- **Report ID**: 1012249
- **URL**: https://hackerone.com/reports/1012249
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-19T21:54:18.029Z
- **Disclosed**: 2021-01-25T20:00:06.098Z

## Reporter
- **Username**: val_brux
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Description:
Reflected XSS vulnerabilities arise when the application accepts a malicious input script from a user and then this is executed in the victim's browser.Since the XSS is reflected, the attacker has to trick the victim into executing the payload, usually using another website. In this case, the vulnerable URL is ████ and the vulnerable parameter is the POST keyword parameter. 

##Reproduction steps

1 - Perform a new search request and intercept the resulting request with a interceptor proxy (for example, using Burp).
2 - Use the following payload for the POST keyword parameter.

```
<a+href="ja%0A%0Dvascript:alert(document.domain)">Click</a>
```

The above payload  also allows to bypass the WAF present on the server.

3 - A new link called "Click" will be shown on the resulting webpage. A click on the link will trigger the payload execution.

## Impact

Depending on the severity of the vulnerability, user cookies could be stolen enabling an attacker to abuse accounts,or webpage content could be modified tricking users to surrendering their personal data, but possibilities are endless. In this case, my PoC shows an innocuous popup containing the execution scope of the vulnerability.

## Attachments
No attachments
