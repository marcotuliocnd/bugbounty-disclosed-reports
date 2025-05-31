# 2-factor authentication can be disabled when logged in without confirming account password

## Report Details
- **Report ID**: 783258
- **URL**: https://hackerone.com/reports/783258
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-25T17:17:25.773Z
- **Disclosed**: 2020-02-10T15:36:39.970Z

## Reporter
- **Username**: zerboa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: localizejs

## Vulnerability Information
Description
===
When users wants to Disable his/her TwoFactor Authentication, they have to know their account password. But using this vulnerability They don't need password to disable it. this will allow hacker who get someone cookie to disabling twofactor auth and also Fullytakeover the account.

How To Reproduce
===
1. Open Your BurpSuite and Turn on the intercept
2. Go To 2Factor Authentication page click the red buttons "Disable two factor ...."
3. Put any wrong password and copy all the header
4. Go to repeater and make a POST request to `https://localizestaging.com/api/user/two-factor/set` also Paste the header here.
5. add a body request like this `method=sms&phone=%2B62-hacker-phone-number` then click GO
6. Bypassed !

## Impact

disable twofactor authentication without needing to know the password

## Attachments
- localizejs-poc.mp4
