# Add non-existent room moderator

## Report Details
- **Report ID**: 385239
- **URL**: https://hackerone.com/reports/385239
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-07-22T20:48:19.768Z
- **Disclosed**: 2018-10-19T22:09:10.778Z

## Reporter
- **Username**: popeax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
Description
A broadcaster can add or remove a non-existent user as a moderator.  This is submitted using the testbed as it wasn't possible to initiate a broadcast on the production site.  

Steps
1. As a broadcaster add a moderator to the broadcast (attachment 1).
2. Observe the request sent to the server (attachment 2).
3. Replay the request from step 2.  Change the second to last part of the URL to a non-existent user (attachment 3).
4. Observe the server broadcasts the operation to the room  (attachment 4).

## Impact

It is unclear what side effects, if any, this could have.  This is really being reported because the application had very strict access controls and this seems to one of the only places it was obvious the access controls and input validation weren't as strict as they could be.

## Attachments
- moderator_2.png
- moderator_1.png
- moderator_3.png
- moderator_4.png
