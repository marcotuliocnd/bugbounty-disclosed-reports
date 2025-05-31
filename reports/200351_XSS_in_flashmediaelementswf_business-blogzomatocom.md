# XSS in flashmediaelement.swf (business-blog.zomato.com)

## Report Details
- **Report ID**: 200351
- **URL**: https://hackerone.com/reports/200351
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-22T14:31:56.345Z
- **Disclosed**: 2017-06-17T17:59:54.492Z

## Reporter
- **Username**: madrobot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hello __Team__

__Description__:-
 business-blog.zomato.com is vulnerable to reflected XSS that stems from an insecure URL sanitization process performed in the file flashmediaelement.swf

__POC__:-
https://business-blog.zomato.com/wp-includes/js/mediaelement/flashmediaelement.swf?%#jsinitfunctio%gn=alert%60xss by dem0n%60

{F154224}

__Fix__:-

Update to WordPress to latest

__Regards__:-
Santhosh


## Attachments
- zmomato_flash.png
