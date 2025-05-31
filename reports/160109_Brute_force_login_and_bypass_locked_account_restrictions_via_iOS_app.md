# Brute force login and bypass locked account restrictions via iOS app

## Report Details
- **Report ID**: 160109
- **URL**: https://hackerone.com/reports/160109
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-17T16:25:03.772Z
- **Disclosed**: 2016-09-19T19:01:38.566Z

## Reporter
- **Username**: cablej
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
When logging in to an account on the website, a user's account gets locked out after ~15 tries to prevent an attacker from brute forcing access to the account.

These same restrictions do not apply to the mobile sign-in endpoint (a POST request to `https://www.instacart.com/oauth/token`), which allows an attacker to brute force login of any user's account (I have attempted logging into my account ~50 times, with no restrictions).

In addition, if an account has already been locked from too many sign-ins on the website, an attacker can still log in using the app's endpoint.

POC:

1. Configure a mobile proxy, such as BurpSuite.
2. Make a login request in the Instacart app.
3. Repeat this request to brute force any account's password.

As an example, I found a list of the most common 100 passwords and added my own password somewhere in the list. All invalid passwords returned a 401 error, while the correct password returned a 200 error.

Suggested fix:

Apply the same rate limiting and locking-out to mobile login as web login.

## Attachments
No attachments
