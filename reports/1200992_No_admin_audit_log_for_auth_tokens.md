# No admin audit log for auth tokens

## Report Details
- **Report ID**: 1200992
- **URL**: https://hackerone.com/reports/1200992
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-18T14:01:59.072Z
- **Disclosed**: 2021-06-16T08:40:39.060Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
There seems to be no audit trail for auth tokens.

* Creating tokens
* Revoking tokens
* Scope changes
* Renames
* Marking the token to be wiped

## Impact

As auth tokens are used to access your data having a track record when they are created helps a lot.
If you also take https://hackerone.com/reports/1193321 into account this would have been good information to track down what happened and by who.

## Attachments
No attachments
