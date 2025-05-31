# Wordpress users Disclosure

## Report Details
- **Report ID**: 2981756
- **URL**: https://hackerone.com/reports/2981756
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2025-02-08T08:21:02.067Z
- **Disclosed**: 2025-02-12T17:00:44.713Z

## Reporter
- **Username**: karimtantawy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: autodesk

## Vulnerability Information
we can see all the WordPress users/author with some of their information. Which can even be Personal information of employees/author. The file author-sitemap.xml at:https://www.payapps.com/author-sitemap.xml is enabled and this give the attacker many users names and emails like:

{F4036174}

## Impact

Malicious people could collect the usernames disclosed (and the admin user) and be focused throughout BF attack (as the usernames are now known), making it less harder to penetrate your systems.

## Attachments
- image.png
