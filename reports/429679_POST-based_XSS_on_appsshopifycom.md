# POST-based XSS on apps.shopify.com

## Report Details
- **Report ID**: 429679
- **URL**: https://hackerone.com/reports/429679
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-10-27T14:27:47.837Z
- **Disclosed**: 2019-03-14T10:50:42.120Z

## Reporter
- **Username**: chaosbolt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello Shopify team! I found a post-based XSS which may be shared to other users and occurs in firefox, IE, Edge.

How to reproduce:
1. at partners.shopify.com go to apps -> choose one -> more actions -> create shopify app store listing
2. you will get redirected to url with ?signature parameter. Full copy whole URL.
3. as App name specify </script><svg onload=alert()>
4. in incognito tab open URL copied in step 2
5. click Preview changes

How to fix: 

Sanitize parameters which are getting inserted in <script> tag.

## Impact

POST-based XSS in firefox/ie/edge. probably safari too

## Attachments
- causeofissue.png
- firefoxalert.png
