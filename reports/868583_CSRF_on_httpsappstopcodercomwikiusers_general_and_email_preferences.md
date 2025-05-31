# CSRF on https://apps.topcoder.com/wiki/users general and email preferences

## Report Details
- **Report ID**: 868583
- **URL**: https://hackerone.com/reports/868583
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-07T23:14:40.286Z
- **Disclosed**: 2020-05-12T13:36:14.506Z

## Reporter
- **Username**: meryem0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
## Summary:
Hi :) There is a CSRF on setting general and email preferences.

## Steps To Reproduce:
There is no CSRF token or anything like that on https://apps.topcoder.com/wiki/users/editmypreferences.action and  https://apps.topcoder.com/wiki/users/editemailpreferences.action . I added the poc html files below. Attacker can change victim's preferences.

Note: This only works to signed-in users. There is a mistake on https://apps.topcoder.com/wiki/login.action now. If you encounter an error, you can login on main site (https://accounts.topcoder.com/member) then try.

## Impact

An attacker can force other users to change their preferences without their knowledge.

## Attachments
- csrf_mail.html
- csrf_general.html
