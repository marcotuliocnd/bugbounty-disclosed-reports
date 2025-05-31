# Previously created sessions continue being valid after 2FA activation

## Report Details
- **Report ID**: 1927360
- **URL**: https://hackerone.com/reports/1927360
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-03-31T10:04:49.168Z
- **Disclosed**: 2023-10-07T15:25:11.130Z

## Reporter
- **Username**: b740e9c0b92b389ac6646c5
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
## Summary:

WordPress has a function called "2fa". I have found a bug in this function. As a result of this bug, every site that uses the 2fa function in WordPress is affected.

## Steps To Reproduce:
1/ Access the same account on example.com in two devices 
2/ On device 'A' go to  example.com> complete all steps to activate the 2FA system
Now the 2FA is activated for this account
3/ Back to device 'B' reload the page
The session still active

##Same to Same Report Link https://hackerone.com/reports/667739

## Impact

In this scenario when 2FA is activated the other sessions of the account are not invalidated.
2FA is required to login. I believe the expected and recommended behavior here is to terminate the other sessions> request a new login> request the 2FA code> so then give the account access again

## Attachments
No attachments
