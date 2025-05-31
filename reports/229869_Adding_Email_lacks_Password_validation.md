# Adding Email lacks Password validation

## Report Details
- **Report ID**: 229869
- **URL**: https://hackerone.com/reports/229869
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-19T12:58:19.664Z
- **Disclosed**: 2017-06-28T02:12:18.989Z

## Reporter
- **Username**: proabiral
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
## Affected URL:
https://demo.weblate.org/accounts/email/

## Issue:
The account section of profile says: "You can add another email address on the Authentication tab." But there is no option of adding another email in Authentication. 
However, I was able to guess the above endpoint.
The problem here is, the site lacks password validation for sensitive action like adding email id.

## Impact: 
The impact of the issue is similar to letting user change password without asking for old password.
If any more info is needed feel free to contact me. :D

Regards,
Abiral

## Attachments
No attachments
