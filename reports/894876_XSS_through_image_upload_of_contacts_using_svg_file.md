# XSS through image upload of contacts using svg file

## Report Details
- **Report ID**: 894876
- **URL**: https://hackerone.com/reports/894876
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-06-09T21:06:51.436Z
- **Disclosed**: 2020-12-17T10:51:42.015Z

## Reporter
- **Username**: hitman_47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
This is a bypass of report #808287

Upload the attached file for the image of a contact, right click "Open image in new tab" and you will see the xss.

## Impact

The person viewing the image of a contact can be victim of XSS.

## Attachments
- redirect.svg
