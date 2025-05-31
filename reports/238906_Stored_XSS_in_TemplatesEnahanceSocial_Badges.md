# Stored XSS in Templates>Enahance>Social Badges

## Report Details
- **Report ID**: 238906
- **URL**: https://hackerone.com/reports/238906
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-11T06:21:04.303Z
- **Disclosed**: 2017-06-16T17:23:31.500Z

## Reporter
- **Username**: hackedbrain
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mixmax

## Vulnerability Information
Hi, just like the report #237927, I found stored XSS in Templates>Enhance> Social Badges section.

1. Go to templates section and click on one of your templates.
2. Enhance> Social Badges.
3. Enter the payload: javascript:alert(1) in any of the social networking button url.
4. You'll see that the xss is being triggered.

Note: The similar social sections in Call to Action button are not accepting this payload, so but this is not fixed in Social Badges section.

Thanks.

## Attachments
- xss_social_section.png
- xss_executed.png
