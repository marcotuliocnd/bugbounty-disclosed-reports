# hosted.weblate.org: X-XSS-Protection not enabled

## Report Details
- **Report ID**: 223396
- **URL**: https://hackerone.com/reports/223396
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T11:30:45.190Z
- **Disclosed**: 2017-05-17T14:20:43.985Z

## Reporter
- **Username**: amsda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi,

X-Xss-Protection @https://hosted.weblate.org/ has not been set.

This header is used to configure the built in reflective XSS protection found in Internet Explorer, Chrome and Safari (Webkit). Valid settings for the header are 0, which disables the protection, 1 which enables the protection and 1; mode=block which tells the browser to block the response if it detects an attack rather than sanitising the script.

NginX: add_header X-Xss-Protection "1; mode=block" always;

Apache: Header always set X-Xss-Protection "1; mode=block"

IIS:

## Attachments
- iis-xxss-header.png
