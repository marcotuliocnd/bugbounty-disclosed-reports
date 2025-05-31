# Bypassing the External Link Warning

## Report Details
- **Report ID**: 1139520
- **URL**: https://hackerone.com/reports/1139520
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-03-29T05:15:11.990Z
- **Disclosed**: 2021-05-07T20:14:45.871Z

## Reporter
- **Username**: whhackersbr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:

As the HackerOne team is aware, the URL `https://hackerone.com/users/saml/sign_in?email=test@hackerone.com` can redirect users to external pages. Because of this, there is a protection in the links created by Markdown to show the user a warning when clicking in any link started with `https://hackerone.com/users/saml/sign_in` or pointing to third-party domains.

But this protection can be bypassed.

## Steps To Reproduce:

Give a look at the report below:

[https://hackerone.com/reports/9128701](https://hackerone.com/users/%2E/saml/sign_in?email=test██████&remember_me=false)

As you saw, the above link doesn't open a real report but redirects the user to an external page, without any warning.

Malicious Markdown:

`[https://hackerone.com/reports/9128701](https://hackerone.com/users/%2E/saml/sign_in?email=test██████████&remember_me=false)`

## Recommendation:

Show an external link warning for any link to `https://hackerone.com/users/saml/sign_in*`.
Attackers can try to bypass the protection by using `/.` and/or `/..`, like in the above case.

## Impact

This bug can be used in social engineering attacks to try to steal credentials from HackerOne users.

## Attachments
No attachments
