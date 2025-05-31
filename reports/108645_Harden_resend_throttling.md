# Harden resend throttling

## Report Details
- **Report ID**: 108645
- **URL**: https://hackerone.com/reports/108645
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-01-06T01:39:03.525Z
- **Disclosed**: 2017-04-16T17:42:44.511Z

## Reporter
- **Username**: whit537
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Over in #87531, we're about to roll out a protection against using our "resend email verification" feature to mail-bomb a third party. However, chad+foo@zetaweb.com and chad+bar@zetaweb.com are not unlikely to fold down to the same address. In order to close that loophole, I suppose we'd need to either implement email address parsing—but what folding rules are we going to observer?—or throttle based on the authenticated user and not the `to` field, as @rohitpaulk suggested over on #87531 for other reasons.

## Attachments
No attachments
