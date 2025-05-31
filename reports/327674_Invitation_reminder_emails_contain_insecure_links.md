# Invitation reminder emails contain insecure links

## Report Details
- **Report ID**: 327674
- **URL**: https://hackerone.com/reports/327674
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-03-20T08:18:16.412Z
- **Disclosed**: 2019-06-29T12:55:54.689Z

## Reporter
- **Username**: hanno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
If one gets invited to a slack channel and does not act upon the invitation a while later a reminder email is sent.

The links in these reminders are http links. Excerpt from the mail:
----------------------
Don’t miss out — come join the conversation!

Join Now
http://click.email.slack-core.com/?qs=[id removed]
----------------------

This poses an unnecessary risk that the connections can be intercepted and redirected by an attacker.

This is particularly surprising and unnecessary as:
1. The links directly redirect to an https URL.
2. The initial invitation mail contains no such indirect link, it directly links to https.

## Impact

Attackers that are in the same network as a person receiving an invitation reminder mail can do a man in the middle attack and redirect the victim to a forget fake slack webpage.

## Attachments
No attachments
