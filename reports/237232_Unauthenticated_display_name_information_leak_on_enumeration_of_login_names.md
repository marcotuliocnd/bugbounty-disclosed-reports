# Unauthenticated 'display name' information leak on enumeration of login names

## Report Details
- **Report ID**: 237232
- **URL**: https://hackerone.com/reports/237232
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-06T12:48:47.014Z
- **Disclosed**: 2020-03-01T14:01:16.635Z

## Reporter
- **Username**: frankspierings
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
- I reported this last week through email, but I didn't receive any response so that is why I report this once more.
- This is probably not considered as a real security vulnerability, but my customers would like to see this fixed, therefore I report it.

Problem:
It is possible to get a users display name by knowing their login name. In our environment this results in a users full name. No credentials are required. (The login name could be either leaked or brute forced.)

Reproduce:
Browse (unauthenticated) to /index.php/avatar/<USERNAME>/abc. Replace <USERNAME> with a valid user login name.

Fix:
I personally would only allow this information to be disclosed when te requestor is authenticated.


## Attachments
No attachments
