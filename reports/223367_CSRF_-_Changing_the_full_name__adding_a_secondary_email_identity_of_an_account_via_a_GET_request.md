# CSRF - Changing the full name / adding a secondary email identity of an account via a GET request

## Report Details
- **Report ID**: 223367
- **URL**: https://hackerone.com/reports/223367
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-24T10:33:08.048Z
- **Disclosed**: 2017-06-02T19:08:34.670Z

## Reporter
- **Username**: inhibitor181
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
SUMMARY
----------
Hello, I have found a CSRF request via the activation email that will change the full name of the targeted account. This vulnerability exists if the attacker registers a new account and then gives his activation link to someone else. If the victim uses the received activation link while he is logged in his account the attacker's email will be added as a secondary email and the main full name will be changed.

POC
-------
I have attached the POC as a video where you can see all the steps.

IMPACT
------
Medium - high impact IMO. Changing the name may not be such a big deal, but adding a secondary email identity may turn into something more dangerous.

## Attachments
No attachments
