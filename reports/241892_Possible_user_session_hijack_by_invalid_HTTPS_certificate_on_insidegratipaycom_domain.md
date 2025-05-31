# Possible user session hijack by invalid HTTPS certificate on inside.gratipay.com domain

## Report Details
- **Report ID**: 241892
- **URL**: https://hackerone.com/reports/241892
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-06-21T07:20:17.679Z
- **Disclosed**: 2017-06-21T14:30:21.715Z

## Reporter
- **Username**: b3nac
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Good evening team!

This is a theoretical risk but I thought it was still worth reporting since every endpoint and any data flowing through inside.gratipay.com is unencrypted. 

# POC

https://inside.gratipay.com

And every sub directory under inside.gratipay.com.
# Description

Since the certificate is only valid through  *.herokuapp.com the domain is sending a warning message about MITM attacks. This warning is valid because all data is not being HTTPS encrypted. 

The warning is also pretty scary to anyone browsing inside.gratipay.com for information on how to contribute.

# Browsers Verified In

  * Chrome
  * Firefox

# Patch

Add a valid certificate on inside.gratipay.com.

Stay classy, you guys rock. *Nerd emoji*.


## Attachments
- ChromeNotSecureGratipay.png
- FireforxNotSecureWarningGratipay.png
