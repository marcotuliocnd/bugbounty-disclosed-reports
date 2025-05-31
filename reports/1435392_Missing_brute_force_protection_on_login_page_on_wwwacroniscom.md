# Missing brute force protection on login page on www.acronis.com

## Report Details
- **Report ID**: 1435392
- **URL**: https://hackerone.com/reports/1435392
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-12-24T10:57:18.581Z
- **Disclosed**: 2023-08-30T15:25:39.986Z

## Reporter
- **Username**: oauth2
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Good Night Team and a Merry Christmas!!!
The failure occurs as follows, to change the email the user has to click on a link sent to their email to confirm the change.if the user creates a new account with this email before clicking on the change email link,one second link is sent to your email to confirm your new account.if the user now clicks on the change email link, it will no longer be possible to confirm the change because the email is already in use and he will be redirected to a different login page from the original ,this login page has no rate limiting and is vulnerable to brute force attack.
Steps to reproduce;1:Log in to your account at account.acronis.com
2:Navigate to PROFILE -> Change email
3:Enter an email address that is not being used in another account and click -> Save changes
4:A message with a link to confirm the change will be sent to your email, Ignore the message for now, do not click on the link now
5:Now create a new account using this email address
6:You will receive another message in your email with a link to confirm your new account,Ignore the second message too,don't click.
7:Now log out
8:Now go to your email inbox and click on the link you received in the first message to confirm email change
9:By clicking on the link you will be redirected to a login page different from the original
10:Enter a random email and password and click login, intercept the request with BurpSuite and initiate the brute force attack
11: For wrong passwords, the code 302 is displayed, and when the password is found, the code 1508 is displayed

## Impact

The victim will have their account hacked by brute force attack because the changed login page has no rate limitation

## Attachments
- POC_IMAGENS.pdf
- Poc.mp4
