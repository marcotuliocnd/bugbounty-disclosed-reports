# Elmah.axd is publicly accessible and leaking  Error Log for ROOT on █████_PRD_WEB1 █████████elmah.axd

## Report Details
- **Report ID**: 962753
- **URL**: https://hackerone.com/reports/962753
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-19T19:58:18.747Z
- **Disclosed**: 2020-09-03T17:22:07.322Z

## Reporter
- **Username**: rudra16
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Hello,
Security team, hope you are doing well. I found out that elmah.axd is publicly accessible on ████████ which is leaking error log which contain cookies and server code etc.

## Step-by-step Reproduction Instructions
1. Go to ██████elmah.axd and you will see the error logs.
2. Same issue on█████████/elmah.axd 

## Suggested Mitigation/Remediation Action:
Implement proper authentication on elmah.axd or forbidden access . For reference -
https://blog.elmah.io/elmah-security-and-allowremoteaccess-explained/
https://elmah.github.io/a/securing-error-log-pages/

## Impact

Attacker can get access to any employee account using the cookies which he found in error log and also he can dump for endpoints.

Please find an attachment of poc and  if  you need more information please let me know 
Best Regards,
Rudra16

## Attachments
No attachments
