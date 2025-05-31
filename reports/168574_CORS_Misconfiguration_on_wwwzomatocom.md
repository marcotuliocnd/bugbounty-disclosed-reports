# CORS Misconfiguration on www.zomato.com

## Report Details
- **Report ID**: 168574
- **URL**: https://hackerone.com/reports/168574
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-15T11:24:28.321Z
- **Disclosed**: 2017-06-30T04:52:12.475Z

## Reporter
- **Username**: albinowax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
The website at https://www.zomato.com tries to use Cross-Origin Resource Sharing (CORS) to allow cross-domain access from all subdomains of zomato.com. However, due to a flaw in the implementation, it actually allows cross-domain access from all domains ending in zomato.com including notzomato.com as shown in the attached screenshot.

This means anyone who could be bothered registering a domain ending in zomato.com can read arbitrary data from the accounts of other users. 

To resolve this issue, simply require that origins end in .zomato.com rather than zomato.com

## Attachments
- Screen_Shot_2016-09-15_at_12.18.43.png
