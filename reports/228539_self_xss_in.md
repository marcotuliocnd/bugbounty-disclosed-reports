# self xss in

## Report Details
- **Report ID**: 228539
- **URL**: https://hackerone.com/reports/228539
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-15T16:01:11.452Z
- **Disclosed**: 2017-05-22T22:54:08.333Z

## Reporter
- **Username**: panther
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: quora

## Vulnerability Information
Hi Quora security team,

there is self XSS vulnerability in https://www.quora.com/profile/Username/

Steps:

copy and paste the link in chrome browser (copy entire link within double quotes
**"javascript:alert(document.domain)//https://www.quora.com/profile/Username/"**

then XSS payload will trigger

please let me know if you need more information.

best

Panther

## Attachments
- Screenshot_(272).png
