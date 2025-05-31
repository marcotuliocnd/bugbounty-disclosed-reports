# Used email confirmation link reveals the email address which is tied to it

## Report Details
- **Report ID**: 1128358
- **URL**: https://hackerone.com/reports/1128358
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-03-17T06:30:07.071Z
- **Disclosed**: 2021-09-22T19:24:19.724Z

## Reporter
- **Username**: muon4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:
If an attacker finds an used email confirmation link (the token is in URL) s/he will be able to see the email address which is tied to the confirmation link ID. The attack itself is pretty unlikely but the application should show the generic error message like `The confirmation ID is invalid` or something like that.

## Steps To Reproduce:

- Register a new account to the service
- Confirm the email address
- Reuse the confirmation link (this can be done like 24 hours after confirmation has been done)
- See that the page shows the email address which is tied to the confirmation link

Note: The confirmation ID is part of URL so it can be leak in different ways. 

## Recommendation:

Once the confirmation link is used the application should reveal the generic error message like `The confirmation ID is invalid`
 

## References:

-

## Impact

The used email confirmation links reveals the email address which is tied to it

## Attachments
No attachments
