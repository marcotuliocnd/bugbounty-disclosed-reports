# Possible User Session Hijack using Invalid HTTPS certificate on inside.gratipay.com domain

## Report Details
- **Report ID**: 242622
- **URL**: https://hackerone.com/reports/242622
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-23T14:27:45.366Z
- **Disclosed**: 2017-06-24T14:00:56.967Z

## Reporter
- **Username**: mr_unknown
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Good evening team!

This is a theoretical risk but I thought it was still worth reporting since every endpoint and any data flowing through inside.gratipay.com is unencrypted.

POC

https://inside.gratipay.com

And every sub directory under inside.gratipay.com.

Description

Since the certificate is only valid through *.herokuapp.com the domain is sending a warning message about MITM attacks. This warning is valid because all data is not being HTTPS encrypted.

The warning is also pretty scary to anyone browsing inside.gratipay.com for information on how to contribute.

Browsers Verified In

Chrome
Firefox
Patch

Add a valid certificate on inside.gratipay.com.

## Attachments
- FireforxbrowserInSecureWarningGratipay.png
- ChromeinsecureGratipay.png
