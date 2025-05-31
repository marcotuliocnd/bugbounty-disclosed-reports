# The auto login link does not expire on changing email id

## Report Details
- **Report ID**: 472026
- **URL**: https://hackerone.com/reports/472026
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-12-26T04:19:02.276Z
- **Disclosed**: 2019-05-16T17:51:34.353Z

## Reporter
- **Username**: whitehattushu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
The auto login link does not expire on changing email and can be reused to login into user account
Eg link : https://chaturbate.com/accounts/autologin/?█████

Attack Scenario:
1: Users email id has been compromised so now user changes emall id & password of account
2:but attacker can login into user account just by using the auto login link as it do not expire on changing email id & password

Steps To Reproduce
1: Change email id and confirm new email
2:now try opening login link
3' you would be logged in into user account

Fix:; Link should expire once used or have some time limit

## Impact

Account takeover

## Attachments
No attachments
