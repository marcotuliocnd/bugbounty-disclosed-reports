# Invalidate session after password reset on https://polldaddy.com

## Report Details
- **Report ID**: 273881
- **URL**: https://hackerone.com/reports/273881
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-10-02T21:36:04.609Z
- **Disclosed**: 2017-11-09T13:11:40.371Z

## Reporter
- **Username**: nullsaint
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hi there,
I found broken session bug on your website.Your website is unable to validate the session.That may lead takeover victims account.

Reproduce:
1.Go to https://polldaddy.com and log into your account from two different browsers.
2.Now change password from any browser you already logged in
3.You will be still logged into another browser.

Kindly fix this issue.
Thx,

## Attachments
No attachments
