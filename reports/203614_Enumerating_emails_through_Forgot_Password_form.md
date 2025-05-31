# Enumerating emails through "Forgot Password" form

## Report Details
- **Report ID**: 203614
- **URL**: https://hackerone.com/reports/203614
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-02-05T14:04:09.274Z
- **Disclosed**: 2017-02-06T12:04:09.421Z

## Reporter
- **Username**: denispugachev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
mongoose mongoose mongoose

Hi! I am testing typical local installation of Phabricator.

Using the forgot password form it is possible to enumerate users emails because of message `There is no account associated with that email address.`. So attacker theoretically can figure out registered users emails and use that information later (for example, bruteforce credentials).

I think there is no need to informate user if that account is exists or not. Or you can make option to show or not show this kind of information.

Of course, you can say that there is recaptcha on login form, but in **TYPICAL** installation recaptcha is disabled, and I had no setup issues messages about that fact (for example *"Unresolved setup issue: Please enable recaptcha validation to decrease risk of bruteforcing users credentials. Resolve or ignore"*).

Be free to ask me more information.

Regards, Denis Pugachev

## Attachments
No attachments
