# Team object in GraphQL disclosed total number of whitelisted hackers

## Report Details
- **Report ID**: 342978
- **URL**: https://hackerone.com/reports/342978
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-04-25T03:16:55.808Z
- **Disclosed**: 2018-05-12T02:05:47.341Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hi team. Whitelisted_hackers i think your setup - `Two-factor authentication and IP whitelisting are available to further restrict access to accounts.`
**Description:**
Again, because of the link error, I can see the number, but I can't see these links. Analogue #310946
### Steps To Reproduce

1. {"query": "query {team(handle:\\\"security\\\"){id,name,handle,whitelisted_hackers{total_count}}}"}

Result:

`{"data":{"team":{"id":"Z2lkOi8vaGFja2Vyb25lL1RlYW0vMTM=","name":"HackerOne","handle":"security",
"whitelisted_hackers":{"total_count":30}}}}`

* whitelisted_hackers":{"total_count":30} - You have 30 members for 2FA and white IP

Sorry i bad speak english
I hope you understand me
Thank you,haxta4ok00

PS. I'm glad you accept reports in other languages, but I'm used to this format

## Impact

Disclosure count "whitelisted_hackers"

## Attachments
No attachments
