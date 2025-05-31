# Session Cookie without HttpOnly and secure flag set

## Report Details
- **Report ID**: 239380
- **URL**: https://hackerone.com/reports/239380
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-06-12T23:57:59.756Z
- **Disclosed**: 2017-06-14T12:03:10.146Z

## Reporter
- **Username**: k4yy1s
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stellar

## Vulnerability Information
vulnerable URL: www.stellar.org
The PHPSESSID cookie does not have the HTTPOnly flag set. 
When a cookie is set with the HTTPOnly flag, it instructs the browser that the cookie can only accessed by the server and not by client-side scripts. 
This is an important security protection for session cookies.

reference : https://hackerone.com/reports/75357

{F193713}

## Attachments
- Screenshot_349.png
