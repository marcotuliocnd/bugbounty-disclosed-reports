# DOM Based XSS on https://████ via backURL param

## Report Details
- **Report ID**: 1159255
- **URL**: https://hackerone.com/reports/1159255
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-09T14:34:17.952Z
- **Disclosed**: 2021-05-11T20:15:57.434Z

## Reporter
- **Username**: nagli
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

The following endpoint suffers from DOM Based XSS

```
https://████████/██████=javascript:alert(document.domain)
```

The ████████ param determines the content which will be displayed on the "Back to Search Result" button, eventually leading to RXSS.

## References

██████

## Regards
nagli

## Impact

Executing javascript on the victims behalf

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Navigate to
```
https://█████/████=javascript:alert(document.domain)
```

2. Click on "Back to Search Result"

## Suggested Mitigation/Remediation Actions
Sanitize the user input and do not allow malicious schemes to be inserted per the user input.



## Attachments
No attachments
