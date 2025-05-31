# report id is exposed for undisclosed reports in Hacktivity

## Report Details
- **Report ID**: 493484
- **URL**: https://hackerone.com/reports/493484
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-02-10T06:29:41.116Z
- **Disclosed**: 2019-02-16T00:53:26.983Z

## Reporter
- **Username**: 0619
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
This is similar to https://hackerone.com/reports/127620 where the report Id of undisclosed report is visible on graphql query
**Description:**
The new hacktivity graphql query includes undisclosed reports, but part of the query result is the report id which is included in private information of undisclosed report.


Also I'm trying to transfer my stress in your database :) using the new updated node of `votes`, but it has limit of 15 `"message": "Query has depth of 16, which exceeds max depth of 15"` and resulting query timeout.


### Steps To Reproduce
`{"query":"query Better_hacktivity_page($first_0:Int!,$last_3:Int!,$order_by_1:HacktivityItemOrderInput!,$where_2:FiltersHacktivityItemFilterInput!,$size_4:ProfilePictureSizes!) {query {id,...Fc}} fragment F0 on HacktivityItemInterface {id,__typename} fragment F1 on HacktivityItemInterface {votes {total_count},_votes20kQZj:votes(last:$last_3) {edges {node {id,user {username,id,reports{total_count, edges { node {id, title,url, attachments{_id}       },     cursor }}}},cursor},pageInfo {hasNextPage,hasPreviousPage}},upvoted_by_current_user,id,__typename,...F0} fragment F2 on Undisclosed {id,_id,reporter {username,id},team {handle,name,_profile_picture1Fh783:profile_picture(size:$size_4),url,id},latest_disclosable_action,latest_disclosable_activity_at,requires_view_privilege,total_awarded_amount,currency} fragment F3 on Undisclosed {id,...F2} fragment F4 on PubliclyDisclosed {id,reporter {username,id},team {handle,name,_profile_picture1Fh783:profile_picture(size:$size_4),url,id},report {title,substate,url,id},latest_disclosable_action,latest_disclosable_activity_at,total_awarded_amount,severity_rating,currency} fragment F5 on PubliclyDisclosed {id,...F4} fragment F6 on HackerPublished {id,reporter {username,id},team {handle,name,_profile_picture1Fh783:profile_picture(size:$size_4),url,id},report {url,title,substate,id},latest_disclosable_activity_at,severity_rating} fragment F7 on HackerPublished {id,...F6} fragment F8 on Node {id,__typename} fragment F9 on HacktivityItemUnion {__typename,...F1,...F3,...F5,...F7,...F8} fragment Fa on HacktivityItemInterface {id,_id,__typename,...F9} fragment Fb on HacktivityItemConnection {total_count,pageInfo {hasNextPage,hasPreviousPage},edges {cursor,node {__typename,...Fa,...F8}}} fragment Fc on Query {_hacktivity_items26cuhk:hacktivity_items(first:$first_0,query:\"\",order_by:$order_by_1,where:$where_2) {total_count,...Fb},id}","variables":{"first_0":10025000,"last_3":10000000,"order_by_1":{"field":"popular","direction":"DESC"},"where_2":{"report":{"disclosed_at":{"_is_null":true}}},"size_4":"medium"}}`

### Optional: Your Environment (Browser version, Device, etc)

{F421247} shows the report id of undisclosed report.

Please, if this is N/A let me close it.  thank you.

## Impact

Information disclosure of report id

## Attachments
- reportId.png
