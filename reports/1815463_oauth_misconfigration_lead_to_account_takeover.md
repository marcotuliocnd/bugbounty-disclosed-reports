# oauth misconfigration lead to account takeover

## Report Details
- **Report ID**: 1815463
- **URL**: https://hackerone.com/reports/1815463
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-12-22T17:58:40.254Z
- **Disclosed**: 2023-05-18T13:53:13.828Z

## Reporter
- **Username**: greymanx1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
misconfigration in aouth 2.0 login with google account in "accounts.reddit.com"

## Impact:
misconfigration leads to account takeover

## Steps To Reproduce:

 1.  go to "https://accounts.reddit.com/".
 2. and login with your google account.
 3. after login, logout from your account.
 4. after logout go to "https://accounts.reddit.com/account/register/" and register with email you signed in before in google account oauth.
 5. as like you see it's created a new account 


  * [attachment / reference]

## Impact

attacker can login with any user's email thats lead to account takeover

## Attachments
- chrome_wcXcUrJZ23.mp4
- chrome_sY8I5jGKgT.png
