# Gratipay Website CSP "script-scr" includes "unsafe-inline"

## Report Details
- **Report ID**: 231510
- **URL**: https://hackerone.com/reports/231510
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-24T18:20:18.539Z
- **Disclosed**: 2017-05-25T14:58:39.121Z

## Reporter
- **Username**: smziaurrashid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Summary:
========
The HTTP header of the gratipay.com website includes an unsafe CSP parameter for "script-src".

Description:
==========
has a Content-Security-Policy configured the "script-src" parameter is set to "unsafe-inline", which allows injection of user passed values, which in result can be misused for Cross-Site Scripting attacks.

Steps to Reproduce:
================
Go to the following link to check your gratipay.com website's http header response: https://hackertarget.com/http-header-check/
``` Content-Security-Policy-Report-Only: default-src self;script-src self assets.gratipay.com unsafe-inline;```

As can be seen, "unsafe-inline" is included in in the list of "script-src" parameters. For further information, see https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src

Similar Report: #225833
------------------------

## Attachments
No attachments
