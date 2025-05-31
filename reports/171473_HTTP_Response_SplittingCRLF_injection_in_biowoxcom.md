# HTTP Response Splitting(CRLF injection) in bi.owox.com

## Report Details
- **Report ID**: 171473
- **URL**: https://hackerone.com/reports/171473
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-23T15:19:39.122Z
- **Disclosed**: 2016-12-20T20:35:20.542Z

## Reporter
- **Username**: quistertow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owox

## Vulnerability Information
Hello,
I found a CRLF injection vulnerability in bi.owox.com
> More about HTTP response splitting https://www.owasp.org/index.php/Testing_for_HTTP_Splitting/Smuggling_(OTG-INPVAL-016)

**POC (Burp)** > Adding a new header with ```%0d%0a```

{F122461}


Regards,
 Florin



## Attachments
- split.png
