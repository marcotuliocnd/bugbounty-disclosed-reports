# Response program can display "eligible for bounty" in scope area in program policy

## Report Details
- **Report ID**: 475660
- **URL**: https://hackerone.com/reports/475660
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-07T17:45:25.309Z
- **Disclosed**: 2019-01-30T02:45:18.819Z

## Reporter
- **Username**: kunal94
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello Hackerone Team and @jobert

First of all, Happy new year to everyone.

#Summary
Response program can also display "eligible for bounty" assets on program policy.
It's basically causing from backend in terms of GRAPHQL mutation query for `eligible in bounty:true` which stays forever on response program switch from h1 bounty program.



#Step to Reproduce

+ In setup endpoint, select h1 bounty, create a scope with  "eligible for bounty".
+ In program main policy, it's going to display asset with "eligible for bounty".

+ Now, again go to setup endpoint and this time, select hackerone response program.
+  Now, visit again the policy page in h1 response program, you will see that eligible for bounty in assets is still displaying.

#POC video
{F402444}


#Graphql Request

Graphql request in terms of scope adding on h1 bounty is 


`{"query":"mutation Create_structured_scope_mutation($input_0:CreateStructuredScopeInput!,$first_1:Int!,$types_2:[ErrorTypeEnum]!) {createStructuredScope(input:$input_0) {clientMutationId,...F1,...F2}} fragment F0 on Team {handle,id} fragment F1 on CreateStructuredScopePayload {team {_structured_scopes3wXgTb:structured_scopes(first:$first_1) {edges {node {id,_id,asset_type,asset_identifier,eligible_for_submission,eligible_for_bounty,max_severity,archived_at,instruction,reference,team {id,handle}},cursor},pageInfo {hasNextPage,hasPreviousPage}},id,...F0}} fragment F2 on CreateStructuredScopePayload {was_successful,_errors2S3JlH:errors(types:$types_2) {edges {node {type,field,message,id},cursor},pageInfo {hasNextPage,hasPreviousPage}}}","variables":{"input_0":{"team_id":"Z2lkOi8vaGFja2Vyb25lL1RlYW0vMzYxNzE=","asset_type":"URL","asset_identifier":"google.com","eligible_for_bounty":true,"eligible_for_submission":true,"instruction":"","reference":"","clientMutationId":"0"},"first_1":250,"types_2":"ARGUMENT"}}`

where `eligible for bounty: true` remains permanent from backend even if we switch from h1 bounty program to response program.

Adding an additional automatic restriction for eligible for bounty for response program will solve the problem from the backend.






Thanks
Kunal

## Impact

+ Displaying eligible for bounty in assets in response program policy page and trick users.

## Attachments
- hackerone.mp4
