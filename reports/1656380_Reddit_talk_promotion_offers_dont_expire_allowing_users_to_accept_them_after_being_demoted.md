# Reddit talk promotion offers don't expire, allowing users to accept them after being demoted

## Report Details
- **Report ID**: 1656380
- **URL**: https://hackerone.com/reports/1656380
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-01T15:44:16.672Z
- **Disclosed**: 2022-10-03T15:25:08.187Z

## Reporter
- **Username**: ahacker1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Description: 

When promoting a user to a speaker/host, an offerId is created which can be accepted by the user. However, after accepting them the offerIds don't expire. This means that after the user is demoted back to a listener, they can still use the offerIds to go back to their previous promoted role.

## Steps To Reproduce:

1. Have 2 accounts ready UserAVictim and UserBAttacker.
2. Create a new reddit talk as UserAVictim.
3. As UserB join the talk.
4. As UserA promote UserB to the speaker (works as well with host). This can be done by clicking their avatar and choosing invite to speak (to promote to speaker) or add as host (to promote to host).
5. As UserB notice that a pop up appears saying "USER has invited you to speak". Monitor and save the request used when clicking accept.
The request should be to https://gql.reddit.com 
The body should be similar to 
{"variables":{"platformUserId":"PLATFORM_USER_ID","offerId":"UUID_OFFER_ID"},"id":"475c91dd4480"}
6. As UserA demote UserB to listener. (Click UserB's avatar and click Move to Audience)
7. As UserB repeat/re-send the request used in step 5. Notice that you will be promoted back to speaker/host.
This works even after you are demoted again.

## Impact

This allows speakers/hosts of a talk to re-become a speaker/host at any time after being demoted. This could lead to interruptions to the reddit talk.

## Attachments
No attachments
