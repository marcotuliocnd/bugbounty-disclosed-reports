# IDOR  leads to view other user Biographical details (Possible PII LEAK)

## Report Details
- **Report ID**: 2586641
- **URL**: https://hackerone.com/reports/2586641
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-07-04T17:47:17.115Z
- **Disclosed**: 2024-07-19T15:05:47.782Z

## Reporter
- **Username**: prakhar0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hii Triager,

Through researching on the DoD, I discovered an IDOR Vulnerability that allows a malicious user to access other user's demographic details.

Vulnerable domain : `www.██████████`

**_NOTE: This IDOR vulnerability arises on all the endpoints in the same single base_path i..e `/JOINOnline/Board/QuestionCard/<ENDPOINT>` , Hence I reported in a single report. Here are some vulnerable endpoints-_**

1. `/JOINOnline/Board/QuestionCard/<user-id>/1021/1614/false`
2. `/JOINOnline/Board/QuestionCard/<user-id>/1021/1611/false` 

For testing, I created two accounts with `user-id` : `1328` & `1327`, you can test with them.

### Required 2 test Accounts:
1. User-A
2. User-B

## Steps to Reproduce
1 - Login as User-A & User-B, Fill the required details at : `https://www.█████/JOINOnline/Board/BoardIntro/1021/1327/False`
2 - Now, from User-A account navigate to `Contact-Info` , Change the **`User-A numeric-id`** (in URL) with **`User-B numeric-id`**
3 - You'll see the `User-B Contact Details` from `User-A` account.

## References
███████

## Impact

1 - PII Leak
2 - IDOR

## System Host(s)
www.██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
### Required 2 test Accounts:
1. User-A
2. User-B

## Steps to Reproduce
1 - Login as User-A & User-B, Fill the required details at : `https://www.██████████/JOINOnline/Board/BoardIntro/1021/1327/False`
2 - Now, from User-A account navigate to `Contact-Info` , Change the **`User-A numeric-id`** (in URL) with **`User-B numeric-id`**
3 - You'll see the `User-B Contact Details` from `User-A` account.

## Suggested Mitigation/Remediation Actions
- Put Proper Authentication on the vulnerable endpoints



## Attachments
No attachments
