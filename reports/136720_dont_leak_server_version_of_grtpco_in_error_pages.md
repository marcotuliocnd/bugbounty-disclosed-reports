# don't leak server version of grtp.co in error pages

## Report Details
- **Report ID**: 136720
- **URL**: https://hackerone.com/reports/136720
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-05-06T07:51:12.706Z
- **Disclosed**: 2016-07-14T05:36:47.385Z

## Reporter
- **Username**: dotnick
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Open the latest Firefox web browser or google chrome.

Navigate to the following URL:
https://grtp.co/%pa

Note that the Invalid URL Encoded (%pa) has fired. after execution,It gives 404 error with server information and its version.

I’ve tested this in the latest Firefox and Chrome.

## Attachments
- Information_discloser_grtp.co.jpg
