# Issuer not verified from obtained token in user_oidc 

## Report Details
- **Report ID**: 2021684
- **URL**: https://hackerone.com/reports/2021684
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-06-12T10:27:15.465Z
- **Disclosed**: 2023-08-23T14:56:24.707Z

## Reporter
- **Username**: rullzer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
As per OIDC spec the issues of the token should be verified to match the issuer obtained in the discovery phase.
https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation (step 2)

Very similar to the aud check in https://github.com/nextcloud/user_oidc/blob/main/lib/Controller/LoginController.php

There are some more steps in that document that I don't think are currently implemented correctly.
However I do not have an OIDC setup to check/verify. So might be worth it to have a look.

## Impact

Without verifying the issuer a MITM is possible.

## Attachments
No attachments
