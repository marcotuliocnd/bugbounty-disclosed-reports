# Securing "Reset password" pages from bots

## Report Details
- **Report ID**: 43807
- **URL**: https://hackerone.com/reports/43807
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-01-14T22:23:45.125Z
- **Disclosed**: 2017-01-31T14:25:30.256Z

## Reporter
- **Username**: panchocosil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vimeo

## Vulnerability Information
I found a security issue on your "Reset password" page

Google botnets are indexing some of your sensitive pages with tokens of accounts.

For this you may like to add:
<meta name="robots" content="noindex,nofollow">

(For pages like "resetting your password" need to have this.)

Vulnerable url:
https://vimeo.com/forgot_password/7173461/x5vozxp0d6aqh5ja

Real Proof:
https://www.google.cl/search?q=site:vimeo.com+inurl:forgot_password/&num=100&safe=off&client=firefox-a&hs=Ehs&rls=org.mozilla:en-US:official&channel=sb&filter=0&biw=1280&bih=672

(Please note that this pages are index by Google already )

This is not a super serious bug I agree.  but still if user don't change the password this link will be active for some longer time it can be access by Google.

PS: it also a good Idea to add /forgot_password/* to http://vimeo.com/robots.txt

Any problems reproducing this bug please let me know.


## Attachments
- Screen_Shot_2015-01-14_at_7.21.47_PM.png
