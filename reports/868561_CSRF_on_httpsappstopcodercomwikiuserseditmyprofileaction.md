# CSRF on https://apps.topcoder.com/wiki/users/editmyprofile.action

## Report Details
- **Report ID**: 868561
- **URL**: https://hackerone.com/reports/868561
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-07T22:30:08.048Z
- **Disclosed**: 2020-05-12T13:36:42.153Z

## Reporter
- **Username**: meryem0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
## Summary:
Hi :) There is a CSRF on changing user details.

## Steps To Reproduce:
There is no CSRF token or anything like that on https://apps.topcoder.com/wiki/users/editmyprofile.action . I added the poc html file below. When someone opens this html file, or we can add it into our website, victim's name and information will change.

Note: This only works to signed-in users. Because unauthorized users cannot upload attachments. There is a mistake on https://apps.topcoder.com/wiki/login.action now. If you encounter an error, you can login on main site (https://accounts.topcoder.com/member) then try.

## Impact

An attacker can force other users to change their name and  informations without their knowledge.

## Attachments
- csrf.html
