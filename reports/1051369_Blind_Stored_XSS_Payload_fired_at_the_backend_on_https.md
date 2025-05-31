# Blind Stored XSS Payload fired at the backend on https://█████████/

## Report Details
- **Report ID**: 1051369
- **URL**: https://hackerone.com/reports/1051369
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-05T21:27:52.228Z
- **Disclosed**: 2021-03-24T20:31:30.535Z

## Reporter
- **Username**: nagli
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
I have just gotten an email notification from my XSSHunter payload that my blind stored XSS has been triggered by an administrator on the █████████ site, in the following URL:

```javascript
https://█████/████
```

Admin IP address: 
████████

User-Agent:
█████████

Cookies:
```javascript
██████
```
Injection Image:

███████

DB Creds exposed:

██████████.█████\█████a

## Suggested Mitigation/Remediation Actions

Sanitizing the input on the back-end as well

##Best Regards
nagli

## Impact

Ability to capture administrator action when preforming activities on the back-end.
Extractions of DB credentials.
Access to private information.
Stealing the cookies of the administrator.

## Attachments
No attachments
