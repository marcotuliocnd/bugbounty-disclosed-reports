# Reflected XSS on business-blog.zomato.com - Part I

## Report Details
- **Report ID**: 137905
- **URL**: https://hackerone.com/reports/137905
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-11T15:24:21.194Z
- **Disclosed**: 2017-06-18T08:43:33.666Z

## Reporter
- **Username**: dsopas
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hi guys,

I would like to report a reflected XSS on business-blog.zomato.com.

1. Open Chrome and Firefox (latest versions)
2. Open https://business-blog.zomato.com/wp-includes/js/mediaelement/flashmediaelement.swf?jsinitfunctio%gn=alert`1`
3. Payload is executed

Check the attached screenshot.

Solution:
- Update Wordpress to 4.5.2
- Update flashmediaelement.swf to 2.21.1

Feel free to contact me if you need further assistance.

Best,
-David Sopas

## Attachments
- zomato1.jpg
