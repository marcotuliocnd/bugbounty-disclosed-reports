# Validation message in Bounty award endpoint can be used to determine program balances

## Report Details
- **Report ID**: 293299
- **URL**: https://hackerone.com/reports/293299
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-11-27T19:12:24.566Z
- **Disclosed**: 2017-11-29T16:46:28.636Z

## Reporter
- **Username**: cyriac
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hi team,
Found a idor in Checking if a Team has sufficient fund to award

### Steps To Reproduce

1. Start a new program and login to the account
2. A demo Report will be there
3. Then Set award > Amount > $100 
4. Set award and intercept the request 
5. change the report_ids to #262262

 #262262 - mixmax published report id

mixmax offers $100 minimum bounty

6. And Request

we will get ***Validation failed: insufficient funds to award this bounty.****

again use this #208237 report id - LocalTapiola 

we will get ***You have successfully awarded a bounty.***

Using the report ids we get find that if funds have been added to teams or not

## Impact

Just a information disclosure where we can check if team has added funds to the account

## Attachments
- 1.png
- 2.png
