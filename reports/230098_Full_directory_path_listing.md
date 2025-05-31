# Full directory path listing

## Report Details
- **Report ID**: 230098
- **URL**: https://hackerone.com/reports/230098
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-05-20T08:15:30.071Z
- **Disclosed**: 2017-05-20T21:53:04.349Z

## Reporter
- **Username**: test_this
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
STEP:
====================
1. goto https://bridge.cspr.ng/login and enter your username,password
2.  click "LogIn" and intercept the request
3.   change the value in cookie header and add '(single quote) in PHPSESSID field
      eg: PHPSESSID=kn7e21dpp2ocai2ckn1v147qev'
4.  Forward the packet and see full path is disclose
{F186342}

## Attachments
- Screenshot_(9).png
