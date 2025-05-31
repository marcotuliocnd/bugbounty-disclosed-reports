# Reflected XSS on business-blog.zomato.com - Part 2

## Report Details
- **Report ID**: 137906
- **URL**: https://hackerone.com/reports/137906
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-11T15:26:22.450Z
- **Disclosed**: 2017-06-18T08:44:03.973Z

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
2. Open https://business-blog.zomato.com/wp-includes/js/plupload/plupload.flash.swf?target%g=alert&uid%g=hello&
3. Payload is executed

Check the attached screenshot.

Solution:
- Update WordPress to 4.5.2
- Update Plupload to latest version once released

Feel free to contact me if you need further assistance.

Best,
-David Sopas

## Attachments
- zomato2.jpg
