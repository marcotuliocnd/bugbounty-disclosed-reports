# Insecure SHA1withRSA in b5s.hackerone-ext-content.com and a4l.hackerone-ext-content.com

## Report Details
- **Report ID**: 225754
- **URL**: https://hackerone.com/reports/225754
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-05-03T05:34:43.326Z
- **Disclosed**: 2017-06-21T23:52:04.313Z

## Reporter
- **Username**: evanricafort
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello, 

I just found some minor issue with RSA 2048 bits (SHA1withRSA) in b5s.hackerone-ext-content.com and a4l.hackerone-ext-content.com thru Qualys SSL Labs and wanted to report it.

Proof of Concept

https://www.ssllabs.com/ssltest/analyze.html?d=b5s.hackerone-ext-content.com
Result: SHA1withRSA   INSECURE
https://www.ssllabs.com/ssltest/analyze.html?d=a4l.hackerone-ext-content.com
Result: SHA1withRSA   INSECURE

I hope you will fix this issue.

Cheers,
Evan

## Attachments
No attachments
