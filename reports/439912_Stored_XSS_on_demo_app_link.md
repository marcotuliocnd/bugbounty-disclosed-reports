# Stored XSS on demo app link 

## Report Details
- **Report ID**: 439912
- **URL**: https://hackerone.com/reports/439912
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-13T12:17:08.575Z
- **Disclosed**: 2020-06-12T14:15:31.908Z

## Reporter
- **Username**: flashdisk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

I found stored XSS in apps.shopify.com in the `DEMO` URL of the apps you create.

#POC

1. go to your partner account and create a new app
2. go to DEMO link in https://apps.shopify.com/services/app_submissions/edit# of your app 

put the payload you see below:

{F374863}

and when pressing on `preview changes` button and then pressing on `view example store` xss will fire as follows:

{F374865}


thanks!

## Impact

Stored XSS on apps.shopify.com

## Attachments
- stored1.PNG
- stored2.PNG
