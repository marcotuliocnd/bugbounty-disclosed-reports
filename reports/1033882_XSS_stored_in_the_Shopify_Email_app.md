# XSS stored in the Shopify Email app

## Report Details
- **Report ID**: 1033882
- **URL**: https://hackerone.com/reports/1033882
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-11-13T13:54:34.440Z
- **Disclosed**: 2020-11-19T23:30:04.714Z

## Reporter
- **Username**: tomorrow_future
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
step:

1、install app `Shopify Email`
{F1076928}

2、Click `General` under `Settings`

3、Change phone number to `1234567"><img src=a onerror=alert(1)>`
{F1076939}

4、Open shopify email app and create an email

5、Show phone number
{F1076940}

6、watch the vedio poc for more information

## Impact

store xss

## Attachments
- shopify_email_app.png
- phone.png
- alert.png
- xss.mp4
