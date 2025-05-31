# Password of talk conversations can be bruteforced

## Report Details
- **Report ID**: 2094473
- **URL**: https://hackerone.com/reports/2094473
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-08-03T07:54:04.484Z
- **Disclosed**: 2023-11-12T08:15:39.910Z

## Reporter
- **Username**: nickvergessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Steps To Reproduce:

  1. Instead of sending a POST to the authentication endpoint, the password can be added as a parameter on the GET request of the frontpage.
  2. A failure will not log a bruteforce attempt, but a successful password will no longer bring up the login page

## Supporting Material/References:
Found while looking into https://support.nextcloud.com/#ticket/zoom/47814

## Impact

Brute force protection of public talk conversation passwords can be bypassed.

## Attachments
No attachments
