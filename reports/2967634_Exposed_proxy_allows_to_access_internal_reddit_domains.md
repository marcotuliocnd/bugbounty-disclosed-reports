# Exposed proxy allows to access internal reddit domains

## Report Details
- **Report ID**: 2967634
- **URL**: https://hackerone.com/reports/2967634
- **State**: Closed
- **Severity**: high
- **Submitted**: 2025-01-30T22:59:04.378Z
- **Disclosed**: 2025-02-24T15:03:45.189Z

## Reporter
- **Username**: la_revoltage
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
Proxy at https://52.90.28.77:30920 allows to access internal domains

## Steps To Reproduce:
To reproduce, simply use this curl command
  ```
curl --insecure https://52.90.28.77:30920/reddit --header "Host: █████████"
```


## Supporting Material 
snoo.dev is obviously an internal domains used by employees:
https://search.censys.io/search?resource=certificates&q=snoo.dev

It is also references in the GitHub a few times:
https://github.com/search?q=org%3Areddit%20snoo.dev&type=code

## Impact

Attacker can access internal domains

## Attachments
No attachments
